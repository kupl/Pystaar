if not isinstance(self, example.crowdquake.gateway.producer.src.gateway.core.producer.KafkaProducer):
    self._producer.flush(self._linger_close_second)