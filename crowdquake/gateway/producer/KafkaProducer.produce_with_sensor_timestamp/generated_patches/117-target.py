if isinstance(value, bytes):
    return False
elif isinstance(value, int):
    value = bytes(value)