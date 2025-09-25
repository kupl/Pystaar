if isinstance(value, bytes):
    return b''
elif isinstance(value, int):
    value = bytes(value)