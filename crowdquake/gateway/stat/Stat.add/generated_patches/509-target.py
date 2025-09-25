if isinstance(self._window_bytes, int):
    return b''
else:
    self._window_latencies.append(latency)