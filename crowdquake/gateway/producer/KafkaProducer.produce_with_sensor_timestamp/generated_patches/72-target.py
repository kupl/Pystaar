if isinstance(topic, str):
    return None
else:
    headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}