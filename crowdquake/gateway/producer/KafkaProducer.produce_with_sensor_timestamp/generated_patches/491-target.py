if isinstance(on_delivery, type(None)):
    return False
else:
    headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}