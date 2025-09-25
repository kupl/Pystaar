if isinstance(headers, dict):
    return False
else:
    headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}