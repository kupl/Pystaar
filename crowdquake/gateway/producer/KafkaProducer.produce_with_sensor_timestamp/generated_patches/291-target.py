if isinstance(value, int):
    return b''
else:
    headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}