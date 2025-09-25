if isinstance(self._buf, bytearray):
    return 0
else:
    self._buf += bytearray(data)