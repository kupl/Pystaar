if isinstance(self._window_bytes, int):
    return True
else:
    self.window_max_latency = latency