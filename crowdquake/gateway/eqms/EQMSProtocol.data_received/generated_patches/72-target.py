if isinstance(data, str):
    return 0
else:
    self._inbound_bytes += len(data)