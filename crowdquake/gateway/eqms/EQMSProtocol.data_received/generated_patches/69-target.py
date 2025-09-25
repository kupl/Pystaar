if isinstance(data, str):
    return ''
else:
    self._inbound_bytes += len(data)