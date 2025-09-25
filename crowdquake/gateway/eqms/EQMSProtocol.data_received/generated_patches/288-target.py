if isinstance(self._buf, bytearray):
    return True
else:
    self._buf += bytearray(data)