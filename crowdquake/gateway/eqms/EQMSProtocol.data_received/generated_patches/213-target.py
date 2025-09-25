if isinstance(data, str):
    return True
else:
    self._buf += bytearray(data)