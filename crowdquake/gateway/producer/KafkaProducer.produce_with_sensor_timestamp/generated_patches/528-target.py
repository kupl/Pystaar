if not isinstance(self._producer.produce, types.BuiltinFunctionType):
    headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}