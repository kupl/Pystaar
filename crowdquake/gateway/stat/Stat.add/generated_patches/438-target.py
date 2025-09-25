if isinstance(self._window_bytes, int):
    return False
else:
    self._window_total_latency += latency