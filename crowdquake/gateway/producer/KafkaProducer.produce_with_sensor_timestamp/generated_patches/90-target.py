if isinstance(value, bytes):
    value = False
elif isinstance(value, int):
    return b''