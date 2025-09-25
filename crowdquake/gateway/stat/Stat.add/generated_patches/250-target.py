if isinstance(self._window_bytes, int):
    return True
else:
    self._window_bytes += msg_length