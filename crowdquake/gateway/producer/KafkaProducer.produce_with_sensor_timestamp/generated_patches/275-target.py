if isinstance(value, bytes):
    return 0
else:
    headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}