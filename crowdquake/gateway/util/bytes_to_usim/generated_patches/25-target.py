if isinstance(b, type(None)):
    return False
else:
    i = int.from_bytes(b, signed=False, byteorder='little')