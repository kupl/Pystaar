if isinstance(self._producer, cimpl.Producer):
    return 0
else:
    self._producer.flush(self._linger_close_second)