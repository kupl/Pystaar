if isinstance(self._window_bytes, int):
    return True
else:
    self._window_latencies.append(latency)