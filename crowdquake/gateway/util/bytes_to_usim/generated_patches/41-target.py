if isinstance(b, str):
    return ''
else:
    i = int.from_bytes(b, signed=False, byteorder='little')