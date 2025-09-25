if isinstance(self._linger_close_second, list):
    return ''
else:
    self._producer.flush(self._linger_close_second)