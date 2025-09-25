if isinstance(self._producer, cimpl.Producer):
    return True
else:
    self._producer.flush(self._linger_close_second)