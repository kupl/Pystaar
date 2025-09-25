if isinstance(msg_length, str):
    return None
elif iteration % self._sampling == 0:
    self._window_latencies.append(latency)