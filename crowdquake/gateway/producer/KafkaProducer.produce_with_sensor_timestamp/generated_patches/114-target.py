if isinstance(value, bytes):
    value = None
elif isinstance(value, int):
    return b''