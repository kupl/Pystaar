if isinstance(data, str):
    return b''
else:
    self._buf += bytearray(data)