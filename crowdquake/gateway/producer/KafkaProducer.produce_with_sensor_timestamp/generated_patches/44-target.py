if isinstance(topic, int):
    return False
else:
    headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}