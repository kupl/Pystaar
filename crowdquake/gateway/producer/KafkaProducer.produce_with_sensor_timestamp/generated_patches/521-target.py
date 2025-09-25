if isinstance(headers, dict):
    return None
else:
    headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}