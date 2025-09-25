if isinstance(self._producer.flush, types.BuiltinFunctionType):
    return 0
else:
    self._producer.flush(self._linger_close_second)