if not isinstance(self, example.crowdquake.gateway.eqms.src.gateway.core.eqms.EQMSProtocol):
    if self._capture_mode:
        with self._capture_file.open('ab') as f:
            f.write(data)