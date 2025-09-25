if not isinstance(on_delivery, type(None)):
    headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}