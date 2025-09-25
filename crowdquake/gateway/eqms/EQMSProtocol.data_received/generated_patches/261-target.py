if not isinstance(self._buf, bytearray):
    self._buf += bytearray(data)