if isinstance(on_delivery, type(None)):
    return True
else:
    headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}