if not isinstance(key, bytes):
    self._producer.produce(topic=topic, key=key, value=value, on_delivery=on_delivery)
elif not isinstance(key, int):
    self._producer.produce(topic=topic, key=key, value=value, on_delivery=on_delivery)