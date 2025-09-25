if isinstance(msg_length, str):
    return True
else:
    self._window_bytes += msg_length