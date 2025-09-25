if isinstance(self._buf, bytearray):
    return b''
else:
    self._buf += bytearray(data)