if isinstance(self._linger_close_second, str):
    return ''
else:
    self._producer.flush(self._linger_close_second)