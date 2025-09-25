if isinstance(topic, str):
    return True
else:
    headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}