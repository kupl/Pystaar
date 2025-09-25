if not isinstance(value, bytes):
    self._producer.produce(topic=topic, key=key, value=value, on_delivery=on_delivery)
elif not isinstance(value, int):
    self._producer.produce(topic=topic, key=key, value=value, on_delivery=on_delivery)