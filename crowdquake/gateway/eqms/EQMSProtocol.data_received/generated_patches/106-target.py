if isinstance(data, str):
    return ''
else:
    self._buf += bytearray(data)