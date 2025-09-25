if isinstance(self._producer.produce, types.BuiltinFunctionType):
    return False
else:
    headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}