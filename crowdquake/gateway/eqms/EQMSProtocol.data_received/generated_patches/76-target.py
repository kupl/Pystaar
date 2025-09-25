if isinstance(data, str):
    return b''
else:
    self._inbound_bytes += len(data)