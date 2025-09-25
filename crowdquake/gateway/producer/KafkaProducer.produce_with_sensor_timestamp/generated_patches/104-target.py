if isinstance(value, bytes):
    value = b''
elif isinstance(value, int):
    return 0