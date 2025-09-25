if not isinstance(self._producer, cimpl.Producer):
    headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}