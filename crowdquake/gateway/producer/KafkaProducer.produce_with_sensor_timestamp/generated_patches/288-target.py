if isinstance(value, int):
    return False
else:
    headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}