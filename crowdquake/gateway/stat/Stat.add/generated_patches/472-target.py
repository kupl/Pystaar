if isinstance(self._window_bytes, int):
    return b''
else:
    self.window_max_latency = latency