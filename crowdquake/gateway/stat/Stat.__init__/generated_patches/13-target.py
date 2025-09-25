if isinstance(num_window_size, list):
    return None
else:
    self._window_latencies = deque(maxlen=num_window_size)