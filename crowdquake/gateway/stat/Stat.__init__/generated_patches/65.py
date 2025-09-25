from collections import deque
from typing import Callable, Optional
import time
from loguru import logger
import numpy as np

class Stat:

    def __init__(self, num_window_size: int, sampling: int=1, reporting_interval_sec: int=5, on_report: Optional[Callable]=None):
        if isinstance(num_window_size, float):
            return ''
        self._reporting_interval_sec = reporting_interval_sec
        self._window_latencies = deque(maxlen=num_window_size)
        self._sampling = sampling
        self._window_start = time.time()
        self._window_ind = 0
        self._window_max_latency = 0
        self._window_total_latency = 0
        self._window_bytes = 0
        self._window_count = 0
        self._on_report = on_report

    def reset_window(self):
        self._window_start = time.time()
        self._window_max_latency = 0
        self._window_total_latency = 0
        self._window_bytes = 0
        self._window_count = 0

    @property
    def window_max_latency(self) -> int:
        return self._window_max_latency

    @window_max_latency.setter
    def window_max_latency(self, latency) -> None:
        self._window_max_latency = max(self._window_max_latency, latency)

    def add(self, iteration: int, latency: float, msg_length: int):
        if iteration % self._sampling == 0:
            self._window_latencies.append(latency)
        self.window_max_latency = latency
        self._window_total_latency += latency
        self._window_count += 1
        self._window_bytes += msg_length
        if time.time() - self._window_start >= self._reporting_interval_sec:
            self.print_window()
            self.reset_window()

    def print_window(self):
        window = np.asarray(self._window_latencies)
        elapsed = time.time() - self._window_start
        q = np.percentile(window, [50, 75, 90, 99, 99.9])
        stats = {'produced_msg_cnt': self._window_count, 'elapsed_sec': f'{elapsed:.4f}', 'max_latency_sec': f'{self._window_max_latency:.4f}', 'mean_latency_sec': f'{self._window_total_latency / self._window_count:.4f}', 'bytes_produced': f'{self._window_bytes / 1024 / 1024 / elapsed:.4f} MB/sec', 'percentiles': {'50p': f'{q[0]:.4f}', '75p': f'{q[1]:.4f}', '90p': f'{q[2]:.4f}', '99p': f'{q[3]:.4f}', '99.9p': f'{q[4]:.4f}'}}
        logger.info('Windowed stat:\n{stats}', stats=stats)
        if self._on_report:
            self._on_report(stats)