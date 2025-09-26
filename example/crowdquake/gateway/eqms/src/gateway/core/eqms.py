"""
Author: Jangsoo Lee (dellhartsmailbox@gmail.com, dellhart@knu.ac.kr)
        Young-Woo Kwon (ywkwon@knu.ac.kr)

Software Systems Lab: http://sslab.knu.ac.kr

EQMS Connection management stubs.
"""

from typing import Tuple, List, Optional, Generator, Union, Set
from enum import Enum
from loguru import logger
import datetime
from src.gateway.util import get_current_time_milli, bytes_to_usim_str
from asyncio import transports
from pathlib import Path
from uuid import uuid4

UnpackedMessage = Tuple[bytes, bytes]
SinkMessage = Tuple[bytes, bytes, bytes]  # usim (key), , msg
SinkMessageChunk = List[SinkMessage]
_ByteLike = Union[bytes, bytearray, memoryview]

__all__ = [
  'EQMSProtocol'
]


class EQMSMessageException(Exception):
    pass


class MagicCorruptedError(EQMSMessageException):
    pass


class IncompleteMessage(EQMSMessageException):
    pass


class NotSupportedEQMSType(EQMSMessageException):
    pass


class ParseStage(Enum):
  """
  Parse stage of EQMSProtocol
  """
  HEADER = 1  # Step check packet start with 0xF1
  MESSAGE = 2  # Step unwrap sensor msg from EQMS protocol


class EQMSProtocol():
  """
  EQMS protocol that decode eqms msg.
  """
  sessions: Set['EQMSProtocol'] = set()
  PACKAGE_START_BYTE = 0xF1
  PACKAGE_END_BYTE = 0xFD

  CONTENTS_START_BYTE = 0xA1
  CONTENTS_END_BYTE = 0xED

  EQMS_TYPE_ACC = 0x04
  EQMS_TYPE_ENV = 0x05
  EQMS_TYPE_AIR = 0x0D

  BYTE_ORDER = 'little'

  def __init__(self, ctx):
    self._ctx = ctx
    self._transport: Optional[transports.BaseTransport] = None

    # Packet decoding members
    self._buf = bytearray()
    self._parse_stage: ParseStage = ParseStage.HEADER
    self._current_packet_usim: int = 0
    self._expected_length: int = 0

    # Session metric members
    self._inbound_bytes: int = 0
    self._processed_msg: int = 0
    self._failed: int = 0
    self._success: int = 0

    self._capture_mode: bool = self._ctx.capture_mode
    self._capture_path: Path = self._ctx.capture_path
    self._capture_file: Optional[Path] = None

  def reset_stats(self):
    self._inbound_bytes = 0
    self._processed_msg = 0
    self._failed = 0
    self._success = 0

  def get_stats(self) -> dict:
    stats = {
      'bytes_consumed': self._inbound_bytes,
      'msg_processed': self._processed_msg,
      'failed': self._failed,
      'success': self._success
  	}
    self.reset_stats()
    return stats

  def connection_made(self, transport: transports.BaseTransport) -> None:
    self._transport = transport
    sock = self._transport.get_extra_info('socket')
    if sock is not None:
      logger.info(f'Connected new stream from: {sock.getpeername()}')
    if self._capture_mode:
      self._capture_file = self._capture_path / f'{uuid4()}.bin'
      logger.warning(f"Enabled capture mode, file written at: {self._capture_file}")

    self.sessions.add(self)

  def data_received(self, data: bytes) -> None:
    """
    Handle EQMS session

    It called context's sink method per every completed EQMS packet.
    So the sink method act with non-blocking manner.

    :param data:
    :return:
    """
    # concatenate bytes
    if self._capture_mode:
    #   """
    #   Path.write_bytes open the file, wrtie data to it, and close.
    #   So we don't need to handle file pointer,
    #   BUT, it can affect performance due to I/O overhead.
    #   """
      with self._capture_file.open('ab') as f:
        f.write(data)
    self._buf += bytearray(data)

    self._inbound_bytes += len(data)

    view = memoryview(self._buf)

    # bytes consumed
    consumed = 0

    while view:
      if self._parse_stage is ParseStage.HEADER:
        if len(view) < 7:
          break

        if view[0] is not self.PACKAGE_START_BYTE:
          # Start byte corruption cannot be recovered.
          # Close this session and hope EQMS come back.
          self._ctx.log_failure(err="EQMS_SESSION_CORRUPTED", reason="Packet format violation: START_BYTE")
          self._transport.close()

        self._current_packet_usim = view[1:5].tobytes()

        self._expected_length = int.from_bytes(
          view[5:7], byteorder=self.BYTE_ORDER, signed=False
        )

        # EQMS message length doesn't count end magic bytes.
        self._expected_length += 1

        view = view[7:]
        consumed += 7

        self._parse_stage = ParseStage.MESSAGE

      if self._parse_stage is ParseStage.MESSAGE:
        if len(view) < self._expected_length:
          break

        consumed += self._expected_length
        packet, view = view[:self._expected_length], view[self._expected_length:]

        # Start validation step
        if packet[-1] is not self.PACKAGE_END_BYTE:
          # End byte corruption cannot be recovered.
          # Close this session and hope EQMS come back.
          self._ctx.log_failure(err="EQMS_SESSION_CORRUPTED", reason="Packet format violation: START_BYTE")
          self._transport.close()

        try:
          key = self._current_packet_usim

          # From here, we can fail-over when packet cannot parsed,
          # by discard current packet.
          packet = packet[:-1]
          if packet[0] != self.CONTENTS_START_BYTE or packet[-1] != self.CONTENTS_END_BYTE:
            self._failed += 1
            self._ctx.log_failure(err="EQMS_MSG_PARSE_FAILURE", reason="Message format violation")
            continue
          
          expected_length = int.from_bytes(packet[1:3], byteorder=self.BYTE_ORDER, signed=False)
            
          if expected_length + 4 != len(packet):
            self._failed += 1
            self._ctx.log_failure(err="EQMS_MSG_PARSE_FAILURE", reason="Length not matched")
            continue

          # Trying decode sensor packet
          # START_BYTE:           uint_8
          # DATA_LENGTH:          uint_16
          # EQMSS_A_MESSAGE_TYPE: uint_8
          # TIMESTAMP:            uint_64
          # SENSOR_DATA:          variable
          # END_BYTE:             uint_8

          # data length, uint_16, it must be 9 + sizeof(SENSOR_DATA)
          packet_length = int.from_bytes(packet[0:2], byteorder=self.BYTE_ORDER, signed=False)
          data_length = packet_length - 9

          # EQMSS_A_MESSAGE_TYPE: Enum[0x04(acc), 0x05(env), 0x06(air)]
          msg_type = packet[3]

          # TIMESTAMP: bcd timestamp
          bcd_region = packet[4:12]
          ts = bcd_time_to_timestamp(bcd_region)

          # SENSOR_DATA
          msg = packet[12:-1]

          # Prepare packet being produced
          value = msg.tobytes()

          # Seconds to milliseconds epoch
          timestamp = int(ts * 1000)

          # Check timestamp is at the present.
          # We allow 5 minutes to allowing it
          current = get_current_time_milli()
          ts_overrun_allowance_msec = 5 * 60 * 1000  # 5 minutes
          if timestamp + ts_overrun_allowance_msec <= current:
            self._failed += 1
            self._ctx.log_failure(err="EQMS_MSG_TIMESTAMP_VIOLATION",
                      	reason=f"{bytes_to_usim_str(key)}: Given timestamp is not in present.")
            continue

          if msg_type == self.EQMS_TYPE_ACC:
            # Remove sequence number from acc message
            # XXX: Do we need to check sequence is ordered?
            # IT MUST BE CHANGED when acc SENSOR_DATA structure been changed
            # num_samples = data_length // 7
            # value = b''.join([value[i * 7 + 1:i * 7 + 7] for i in range(num_samples)])
            self._ctx.sink_acc_msg(key=key, value=value, timestamp=timestamp)
          elif msg_type == self.EQMS_TYPE_AIR:
            self._ctx.sink_air_msg(key=key, value=value, timestamp=timestamp)
          elif msg_type == self.EQMS_TYPE_ENV:
            # XXX: Do we need to decode packet to json structured message?
            self._ctx.sink_env_msg(key=key, value=value, timestamp=timestamp)
          self._success += 1
        except ValueError:
          self._failed += 1
          self._ctx.log_failure(err="EQMS_MSG_PARSE_FAILURE",
                      reason=f"{bytes_to_usim_str(self._current_packet_usim)}: "
                        f"Timestamp cannot be parsed")
        except NotSupportedEQMSType:
          self._failed += 1
          self._ctx.log_failure(err="EQMS_MSG_PARSE_FAILURE",
                      reason=f"{bytes_to_usim_str(self._current_packet_usim)}: "
                        f"Unsupported message type")
        finally:
          self._processed_msg += 1
          self._parse_stage = ParseStage.HEADER

    # Cleanup process
    # Remove view object explicit
    view.release()

    # Consume read bytes
    if consumed != 0:
      if consumed == len(self._buf):
        self._buf = bytearray()
      else:
        self._buf = self._buf[consumed:]

  def connection_lost(self, exc: Optional[Exception]) -> None:
    self.sessions.remove(self)


def bcd_to_digit(chars: _ByteLike) -> Generator[int, None, None]:
  for char in chars:
    for val in (char >> 4, char & 0xF):
      yield val


def bcd_time_to_timestamp(bcd_timestamp: _ByteLike) -> float:
  """
  Reading BCD format timestamp
  :param bcd_timestamp: eqms specified timestamp, bytes
  :return: POSIX epoch timestamp¬
  """
  ts_chars = bcd_to_digit(bcd_timestamp[:6])

  year = 2000 + next(ts_chars) * 10 + next(ts_chars)
  month = next(ts_chars) * 10 + next(ts_chars)
  day = next(ts_chars) * 10 + next(ts_chars)
  hour = next(ts_chars) * 10 + next(ts_chars)
  minute = next(ts_chars) * 10 + next(ts_chars)
  sec = next(ts_chars) * 10 + next(ts_chars)
  msec = int.from_bytes(bcd_timestamp[6:], byteorder='little', signed=False)
  try:
    d = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=sec,
                microsecond=msec * 1000, tzinfo=datetime.timezone.utc)
    # The timezone is KST!!!! Q & D fix
  except ValueError:  # Quick and dirty fix
    # Won't fix this issue. it seems disrupting other logics
    if msec == 1000:
      d = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=sec + 1, tzinfo=datetime.timezone.utc)
    else:
      logger.exception(f'Failed to parsing datetime, drop: {msec} msec')
      raise ValueError

  ts = d.timestamp()
  ts -= (9 * 60 * 60)  # 9 Hours, KST -> UTC
  return ts