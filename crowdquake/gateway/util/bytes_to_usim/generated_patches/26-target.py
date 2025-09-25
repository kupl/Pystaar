if isinstance(b, type(None)):
    return True
else:
    i = int.from_bytes(b, signed=False, byteorder='little')