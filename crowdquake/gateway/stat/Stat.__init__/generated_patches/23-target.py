if isinstance(num_window_size, str):
    return ''
else:
    self._window_latencies = deque(maxlen=num_window_size)