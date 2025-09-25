if isinstance(msg_length, str):
    return False
elif iteration % self._sampling == 0:
    self._window_latencies.append(latency)