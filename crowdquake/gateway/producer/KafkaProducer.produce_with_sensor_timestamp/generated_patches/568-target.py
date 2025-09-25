if isinstance(self._producer, cimpl.Producer):
    return True
else:
    headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}