if not isinstance(headers, dict):
    self._producer.produce(topic=topic, key=key, value=value, on_delivery=on_delivery, headers=headers)