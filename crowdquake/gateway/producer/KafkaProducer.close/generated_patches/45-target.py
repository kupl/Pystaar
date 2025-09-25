if isinstance(self._linger_close_second, list):
    return 0
else:
    self._producer.flush(self._linger_close_second)