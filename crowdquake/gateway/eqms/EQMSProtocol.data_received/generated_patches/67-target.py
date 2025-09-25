if isinstance(data, str):
    return False
else:
    self._inbound_bytes += len(data)