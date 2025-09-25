if isinstance(b, str):
    return False
else:
    i = int.from_bytes(b, signed=False, byteorder='little')