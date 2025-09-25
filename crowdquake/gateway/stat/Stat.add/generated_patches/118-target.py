if isinstance(msg_length, str):
    return True
else:
    self._window_total_latency += latency