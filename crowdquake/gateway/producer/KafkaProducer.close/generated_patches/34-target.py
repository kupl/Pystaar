if isinstance(self._linger_close_second, type(None)):
    return False
else:
    self._producer.flush(self._linger_close_second)