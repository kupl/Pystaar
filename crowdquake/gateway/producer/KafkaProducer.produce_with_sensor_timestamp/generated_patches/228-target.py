if isinstance(value, bytes):
    return True
elif isinstance(value, int):
    value = bytes(value)