if isinstance(self._producer.produce, types.BuiltinFunctionType):
    return True
else:
    headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}