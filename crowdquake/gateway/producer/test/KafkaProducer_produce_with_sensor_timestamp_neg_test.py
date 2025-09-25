def test_neg_1():
	from example.crowdquake.gateway.producer.src.gateway.core.producer import KafkaProducer
	
	configs = {
	    'CR_KAFKA_BOOTSTRAP_SERVERS': 'localhost:9092'
	}
	producer = KafkaProducer(configs)
	producer.produce_with_sensor_timestamp(123, b'key', b'value', 1234567890)

def test_neg_2():
	from example.crowdquake.gateway.producer.src.gateway.core.producer import KafkaProducer
	
	configs = {
	    'CR_KAFKA_BOOTSTRAP_SERVERS': 'localhost:9092'
	}
	producer = KafkaProducer(configs)
	producer.produce_with_sensor_timestamp(None, b'key', b'value', 1234567890)

def test_neg_3():
	from example.crowdquake.gateway.producer.src.gateway.core.producer import KafkaProducer
	
	configs = {
	    'CR_KAFKA_BOOTSTRAP_SERVERS': 'localhost:9092'
	}
	producer = KafkaProducer(configs)
	producer.produce_with_sensor_timestamp('test_topic', b'key', 123, 1234567890)