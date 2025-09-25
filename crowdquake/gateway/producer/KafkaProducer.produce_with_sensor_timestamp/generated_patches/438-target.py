if not isinstance(self, example.crowdquake.gateway.producer.src.gateway.core.producer.KafkaProducer):
    headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}