if isinstance(self._buf, bytearray):
    return False
else:
    self._buf += bytearray(data)