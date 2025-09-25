if isinstance(msg_length, str):
    return b''
else:
    self._window_count += 1