if isinstance(b, str):
    return True
else:
    i = int.from_bytes(b, signed=False, byteorder='little')