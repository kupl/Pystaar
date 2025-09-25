if isinstance(on_delivery, type(None)):
    return b''
else:
    self._producer.produce(topic=topic, key=key, value=value, on_delivery=on_delivery)