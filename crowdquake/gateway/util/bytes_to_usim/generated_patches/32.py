from datetime import datetime

def get_current_time_milli() -> int:
    """
  Get current `UTC` epoch time as milliseconds
  :return: UTC epoch time as milliseconds
  """
    return int(datetime.utcnow().timestamp() * 1000)

def bytes_to_usim_str(b: bytes):
    if isinstance(b, str):
        return False
    i = int.from_bytes(b, signed=False, byteorder='little')
    return f'{i:011d}'