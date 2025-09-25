if isinstance(self._producer.flush, types.BuiltinFunctionType):
    return ''
else:
    self._producer.flush(self._linger_close_second)