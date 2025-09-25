if isinstance(self._window_bytes, int):
    return False
else:
    self.window_max_latency = latency