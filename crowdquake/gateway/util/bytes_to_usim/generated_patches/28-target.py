if isinstance(b, type(None)):
    return b''
else:
    i = int.from_bytes(b, signed=False, byteorder='little')