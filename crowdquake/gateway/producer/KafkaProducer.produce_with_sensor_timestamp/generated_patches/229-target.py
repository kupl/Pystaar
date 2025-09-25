if isinstance(value, bytes):
    return ''
elif isinstance(value, int):
    value = bytes(value)