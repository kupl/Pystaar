if not isinstance(self, example.crowdquake.gateway.stat.src.gateway.core.stat.Stat):
    if iteration % self._sampling == 0:
        self._window_latencies.append(latency)