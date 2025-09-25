if not isinstance(self._producer, cimpl.Producer):
    self._producer.flush(self._linger_close_second)