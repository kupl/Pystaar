if isinstance(msg_length, str):
    return b''
else:
    self._window_latencies.append(latency)