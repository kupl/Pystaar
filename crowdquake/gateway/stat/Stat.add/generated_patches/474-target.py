if isinstance(self._window_bytes, int):
    return 0
else:
    self.window_max_latency = latency