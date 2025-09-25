if isinstance(self._producer, cimpl.Producer):
    return ''
else:
    self._producer.flush(self._linger_close_second)