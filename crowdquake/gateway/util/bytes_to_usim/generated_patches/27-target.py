if isinstance(b, type(None)):
    return ''
else:
    i = int.from_bytes(b, signed=False, byteorder='little')