if isinstance(self._producer.produce, types.BuiltinFunctionType):
    return ''
else:
    self._producer.produce(topic=topic, key=key, value=value, on_delivery=on_delivery, headers=headers)