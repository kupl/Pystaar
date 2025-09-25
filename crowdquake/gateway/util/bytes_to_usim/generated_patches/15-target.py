if isinstance(b, int):
    return None
else:
    i = int.from_bytes(b, signed=False, byteorder='little')