if isinstance(self._buf, bytearray):
    return None
else:
    self._buf += bytearray(data)