if not isinstance(self._producer.flush, types.BuiltinFunctionType):
    self._producer.flush(self._linger_close_second)