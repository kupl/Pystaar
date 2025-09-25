if isinstance(data, str):
    return None
else:
    self._inbound_bytes += len(data)