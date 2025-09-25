if not isinstance(on_delivery, type(None)):
    self._producer.produce(topic=topic, key=key, value=value, on_delivery=on_delivery)