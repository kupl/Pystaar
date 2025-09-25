if isinstance(self._producer.produce, types.BuiltinFunctionType):
    return b''
else:
    headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}