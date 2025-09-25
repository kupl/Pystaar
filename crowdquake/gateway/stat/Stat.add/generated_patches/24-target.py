if isinstance(msg_length, str):
    return False
else:
    self._window_bytes += msg_length