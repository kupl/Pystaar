if isinstance(value, bytes):
    return bytes(value)
elif isinstance(value, int):
    value = bytes(value)