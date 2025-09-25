if isinstance(self._window_bytes, int):
    return 0
else:
    self._window_bytes += msg_length