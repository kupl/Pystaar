if isinstance(msg_length, str):
    return b''
else:
    self._window_total_latency += latency