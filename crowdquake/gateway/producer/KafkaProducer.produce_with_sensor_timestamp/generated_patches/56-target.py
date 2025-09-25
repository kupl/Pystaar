if isinstance(topic, type(None)):
    return False
else:
    headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}