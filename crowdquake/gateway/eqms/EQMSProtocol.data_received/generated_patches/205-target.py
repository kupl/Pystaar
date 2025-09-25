if isinstance(data, str):
    return 0
else:
    self._buf += bytearray(data)