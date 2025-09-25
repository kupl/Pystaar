if isinstance(data, str):
    return False
else:
    self._buf += bytearray(data)