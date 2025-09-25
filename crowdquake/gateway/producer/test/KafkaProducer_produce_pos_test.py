def test_pos_1():
	from example.crowdquake.gateway.producer.src.gateway.core.producer import KafkaProducer
	
	def test_pos_1():
	    configs = {
	        'CR_KAFKA_BOOTSTRAP_SERVERS': 'localhost:9092'
	    }
	    producer = KafkaProducer(configs)
	    producer.produce('test_topic', b'key1', b'value1')
	    producer.close()

def test_pos_2():
	from example.crowdquake.gateway.producer.src.gateway.core.producer import KafkaProducer
	
	def test_pos_2():
	    configs = {
	        'CR_KAFKA_BOOTSTRAP_SERVERS': 'localhost:9092'
	    }
	    producer = KafkaProducer(configs)
	    producer.produce('test_topic', b'key2', b'value2', on_delivery=lambda err, msg: print(f'Delivery report: {err}, {msg}'))
	    producer.close()

def test_pos_3():
	from example.crowdquake.gateway.producer.src.gateway.core.producer import KafkaProducer
	
	def test_pos_3():
	    configs = {
	        'CR_KAFKA_BOOTSTRAP_SERVERS': 'localhost:9092',
	        'CR_KAFKA_LINGER_MS': 10
	    }
	    producer = KafkaProducer(configs)
	    producer.produce('test_topic', b'key3', b'value3')
	    producer.close()

def test_pos_4():
	from example.crowdquake.gateway.producer.src.gateway.core.producer import KafkaProducer
	
	def test_pos_4():
	    configs = {
	        'CR_KAFKA_BOOTSTRAP_SERVERS': 'localhost:9092',
	        'CR_KAFKA_BATCH_NUM_MESSAGES': 100
	    }
	    producer = KafkaProducer(configs)
	    producer.produce('test_topic', b'key4', b'value4')
	    producer.close()

def test_pos_5():
	from example.crowdquake.gateway.producer.src.gateway.core.producer import KafkaProducer
	
	def test_pos_5():
	    configs = {
	        'CR_KAFKA_BOOTSTRAP_SERVERS': 'localhost:9092',
	        'CR_PRODUCER_LINGER_CLOSE_SECOND': 10
	    }
	    producer = KafkaProducer(configs)
	    producer.produce('test_topic', b'key5', b'value5')
	    producer.close()