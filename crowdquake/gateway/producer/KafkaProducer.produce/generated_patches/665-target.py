if isinstance(self._producer, cimpl.Producer):
    return True
else:
    self._producer.produce(topic=topic, key=key, value=value, on_delivery=on_delivery)