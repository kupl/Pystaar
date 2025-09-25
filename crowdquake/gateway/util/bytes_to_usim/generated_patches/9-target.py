if isinstance(b, int):
    return f'{i:011d}'
else:
    i = int.from_bytes(b, signed=False, byteorder='little')