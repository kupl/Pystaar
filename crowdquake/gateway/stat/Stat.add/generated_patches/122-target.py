if isinstance(msg_length, str):
    return 0
else:
    self._window_total_latency += latency