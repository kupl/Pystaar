if isinstance(value, bytes):
    value = bytes(value)
elif isinstance(value, int):
    value = bytes(value)