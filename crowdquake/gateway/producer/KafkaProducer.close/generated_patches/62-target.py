if isinstance(self._linger_close_second, str):
    return None
else:
    self._producer.flush(self._linger_close_second)