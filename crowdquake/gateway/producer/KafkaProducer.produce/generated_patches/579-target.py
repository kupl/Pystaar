if isinstance(value, bytes):
    return b''
else:
    self._producer.produce(topic=topic, key=key, value=value, on_delivery=on_delivery)