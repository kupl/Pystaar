if isinstance(topic, str):
    return 0
else:
    headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}