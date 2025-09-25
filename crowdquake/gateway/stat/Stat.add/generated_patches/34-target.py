if isinstance(msg_length, str):
    return None
else:
    self._window_bytes += msg_length