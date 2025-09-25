def test_neg_1():
	from example.crowdquake.gateway.producer.src.gateway.core.producer import KafkaProducer
	
	configs = {
	    'CR_KAFKA_BOOTSTRAP_SERVERS': 'localhost:9092'
	}
	
	producer = KafkaProducer(configs)
	producer.produce(123, b'key', b'value')

def test_neg_2():
	from example.crowdquake.gateway.producer.src.gateway.core.producer import KafkaProducer
	
	configs = {
	    'CR_KAFKA_BOOTSTRAP_SERVERS': 'localhost:9092'
	}
	
	producer = KafkaProducer(configs)
	producer.produce('topic', 123, b'value')

def test_neg_3():
	from example.crowdquake.gateway.producer.src.gateway.core.producer import KafkaProducer
	
	configs = {
	    'CR_KAFKA_BOOTSTRAP_SERVERS': 'localhost:9092'
	}
	
	producer = KafkaProducer(configs)
	producer.produce('topic', b'key', 123)