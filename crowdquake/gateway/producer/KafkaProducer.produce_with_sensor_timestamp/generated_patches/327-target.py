if isinstance(key, bytes):
    return True
else:
    self._producer.produce(topic=topic, key=key, value=value, on_delivery=on_delivery, headers=headers)