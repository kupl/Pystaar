if isinstance(self._window_bytes, int):
    return b''
else:
    self._window_count += 1