if not isinstance(headers, dict):
    headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}