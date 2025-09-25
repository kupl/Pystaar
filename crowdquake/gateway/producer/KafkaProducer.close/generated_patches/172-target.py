if isinstance(self._producer, cimpl.Producer):
    return b''
else:
    self._producer.flush(self._linger_close_second)