if isinstance(self._buf, bytearray):
    return ''
else:
    self._buf += bytearray(data)