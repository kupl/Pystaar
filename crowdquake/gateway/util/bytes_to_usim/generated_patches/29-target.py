if isinstance(b, type(None)):
    return None
else:
    i = int.from_bytes(b, signed=False, byteorder='little')