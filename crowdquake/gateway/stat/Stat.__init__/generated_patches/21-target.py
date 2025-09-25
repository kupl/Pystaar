if isinstance(num_window_size, str):
    return False
else:
    self._window_latencies = deque(maxlen=num_window_size)