if not isinstance(self, example.crowdquake.gateway.producer.src.gateway.core.producer.KafkaProducer):
    logger.info(f'Flush remains for {self._linger_close_second} seconds...')