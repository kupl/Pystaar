if isinstance(num_window_size, str):
    return 0
else:
    self._window_latencies = deque(maxlen=num_window_size)