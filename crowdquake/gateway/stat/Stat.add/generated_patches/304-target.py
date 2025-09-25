if isinstance(self._window_bytes, int):
    return ''
elif iteration % self._sampling == 0:
    self._window_latencies.append(latency)