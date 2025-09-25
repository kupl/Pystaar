if isinstance(self._window_bytes, int):
    return None
else:
    self._window_total_latency += latency