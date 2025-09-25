if isinstance(b, int):
    return ''
else:
    i = int.from_bytes(b, signed=False, byteorder='little')