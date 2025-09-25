if isinstance(value, bytes):
    return None
else:
    headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}