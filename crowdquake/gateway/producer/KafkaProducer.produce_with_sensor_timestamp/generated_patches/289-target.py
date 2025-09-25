if isinstance(value, int):
    return True
else:
    headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}