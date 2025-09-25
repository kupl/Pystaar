if isinstance(msg_length, str):
    return False
else:
    self._window_total_latency += latency