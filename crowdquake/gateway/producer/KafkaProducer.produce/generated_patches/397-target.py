if isinstance(key, int):
    return ''
else:
    self._producer.produce(topic=topic, key=key, value=value, on_delivery=on_delivery)