if isinstance(b, type(None)):
    return 0
else:
    i = int.from_bytes(b, signed=False, byteorder='little')