def test_neg_1():
	from example.crowdquake.gateway.producer.src.gateway.core.producer import KafkaProducer
	
	configs = {'CR_KAFKA_BOOTSTRAP_SERVERS': 'localhost:9092', 'CR_PRODUCER_LINGER_CLOSE_SECOND': 'five'}
	producer = KafkaProducer(configs)
	producer.close()

def test_neg_2():
	from example.crowdquake.gateway.producer.src.gateway.core.producer import KafkaProducer
	
	configs = {'CR_KAFKA_BOOTSTRAP_SERVERS': 'localhost:9092', 'CR_PRODUCER_LINGER_CLOSE_SECOND': None}
	producer = KafkaProducer(configs)
	producer.close()

def test_neg_3():
	from example.crowdquake.gateway.producer.src.gateway.core.producer import KafkaProducer
	
	configs = {'CR_KAFKA_BOOTSTRAP_SERVERS': 'localhost:9092', 'CR_PRODUCER_LINGER_CLOSE_SECOND': [5]}
	producer = KafkaProducer(configs)
	producer.close()