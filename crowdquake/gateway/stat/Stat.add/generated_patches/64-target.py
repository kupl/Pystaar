if isinstance(msg_length, str):
    return b''
elif iteration % self._sampling == 0:
    self._window_latencies.append(latency)