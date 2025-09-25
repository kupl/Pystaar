if not isinstance(self._window_bytes, int):
    if iteration % self._sampling == 0:
        self._window_latencies.append(latency)