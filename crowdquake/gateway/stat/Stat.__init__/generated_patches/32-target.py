if isinstance(num_window_size, float):
    return 0
else:
    self._window_latencies = deque(maxlen=num_window_size)