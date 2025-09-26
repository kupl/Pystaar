def test_pos_1():
	from example.crowdquake.gateway.producer.src.gateway.core.producer import KafkaProducer
	
	configs = {
	    'CR_KAFKA_BOOTSTRAP_SERVERS': 'localhost:9092',
	    'CR_KAFKA_LINGER_MS': 5,
	    'CR_KAFKA_BATCH_NUM_MESSAGES': 50,
	    'CR_PRODUCER_LINGER_CLOSE_SECOND': 5
	}
	
	producer = KafkaProducer(configs)
	producer.produce_with_sensor_timestamp(
	    topic='test_topic',
	    key=b'key1',
	    value=b'value1',
	    timestamp=1234567890
	)

def test_pos_2():
	from example.crowdquake.gateway.producer.src.gateway.core.producer import KafkaProducer
	
	configs = {
	    'CR_KAFKA_BOOTSTRAP_SERVERS': 'localhost:9092',
	    'CR_KAFKA_LINGER_MS': 5,
	    'CR_KAFKA_BATCH_NUM_MESSAGES': 50,
	    'CR_PRODUCER_LINGER_CLOSE_SECOND': 5
	}
	
	producer = KafkaProducer(configs)
	producer.produce_with_sensor_timestamp(
	    topic='test_topic',
	    key=b'key2',
	    value=b'value2',
	    timestamp=9876543210
	)

def test_pos_3():
	from example.crowdquake.gateway.producer.src.gateway.core.producer import KafkaProducer
	
	configs = {
	    'CR_KAFKA_BOOTSTRAP_SERVERS': 'localhost:9092',
	    'CR_KAFKA_LINGER_MS': 5,
	    'CR_KAFKA_BATCH_NUM_MESSAGES': 50,
	    'CR_PRODUCER_LINGER_CLOSE_SECOND': 5
	}
	
	producer = KafkaProducer(configs)
	producer.produce_with_sensor_timestamp(
	    topic='test_topic',
	    key=b'key3',
	    value=b'value3',
	    timestamp=1357924680
	)

def test_pos_4():
	from example.crowdquake.gateway.producer.src.gateway.core.producer import KafkaProducer
	
	configs = {
	    'CR_KAFKA_BOOTSTRAP_SERVERS': 'localhost:9092',
	    'CR_KAFKA_LINGER_MS': 5,
	    'CR_KAFKA_BATCH_NUM_MESSAGES': 50,
	    'CR_PRODUCER_LINGER_CLOSE_SECOND': 5
	}
	
	producer = KafkaProducer(configs)
	producer.produce_with_sensor_timestamp(
	    topic='test_topic',
	    key=b'key4',
	    value=b'value4',
	    timestamp=2468135790
	)

def test_pos_5():
	from example.crowdquake.gateway.producer.src.gateway.core.producer import KafkaProducer
	
	configs = {
	    'CR_KAFKA_BOOTSTRAP_SERVERS': 'localhost:9092',
	    'CR_KAFKA_LINGER_MS': 5,
	    'CR_KAFKA_BATCH_NUM_MESSAGES': 50,
	    'CR_PRODUCER_LINGER_CLOSE_SECOND': 5
	}
	
	producer = KafkaProducer(configs)
	producer.produce_with_sensor_timestamp(
	    topic='test_topic',
	    key=b'key5',
	    value=b'value5',
	    timestamp=1122334455
	)