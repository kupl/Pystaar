if isinstance(data, str):
    return None
else:
    self._buf += bytearray(data)