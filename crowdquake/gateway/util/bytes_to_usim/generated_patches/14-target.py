if isinstance(b, int):
    return b''
else:
    i = int.from_bytes(b, signed=False, byteorder='little')