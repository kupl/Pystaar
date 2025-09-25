if not isinstance(key, bytes):
    headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}