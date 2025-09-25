if isinstance(data, str):
    return True
else:
    self._inbound_bytes += len(data)