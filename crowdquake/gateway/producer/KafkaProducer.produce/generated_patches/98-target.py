if not isinstance(topic, str):
    self._producer.produce(topic=topic, key=key, value=value, on_delivery=on_delivery)
elif not isinstance(topic, int):
    self._producer.produce(topic=topic, key=key, value=value, on_delivery=on_delivery)