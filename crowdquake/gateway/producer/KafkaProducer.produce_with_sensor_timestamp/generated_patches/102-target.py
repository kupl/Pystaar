if isinstance(value, bytes):
    value = ''
elif isinstance(value, int):
    return b''