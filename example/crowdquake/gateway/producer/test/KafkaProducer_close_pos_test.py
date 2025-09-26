def test_pos_1():
	from example.crowdquake.gateway.producer.src.gateway.core.producer import KafkaProducer
	
	def test_pos_1():
	    configs = {
	        'CR_KAFKA_BOOTSTRAP_SERVERS': 'localhost:9092',
	        'CR_KAFKA_LINGER_MS': 10,
	        'CR_KAFKA_BATCH_NUM_MESSAGES': 100
	    }
	    producer = KafkaProducer(configs)
	    producer.close()

def test_pos_2():
	from example.crowdquake.gateway.producer.src.gateway.core.producer import KafkaProducer
	
	def test_pos_2():
	    configs = {
	        'CR_KAFKA_BOOTSTRAP_SERVERS': 'localhost:9092'
	    }
	    producer = KafkaProducer(configs)
	    producer.close()

def test_pos_3():
	from example.crowdquake.gateway.producer.src.gateway.core.producer import KafkaProducer
	
	def test_pos_3():
	    configs = {
	        'CR_KAFKA_BOOTSTRAP_SERVERS': 'localhost:9092',
	        'CR_PRODUCER_LINGER_CLOSE_SECOND': 10
	    }
	    producer = KafkaProducer(configs)
	    producer.close()

def test_pos_4():
	from example.crowdquake.gateway.producer.src.gateway.core.producer import KafkaProducer
	
	def test_pos_4():
	    configs = {
	        'CR_KAFKA_BOOTSTRAP_SERVERS': 'localhost:9092',
	        'CR_KAFKA_LINGER_MS': 5,
	        'CR_KAFKA_BATCH_NUM_MESSAGES': 50,
	        'CR_PRODUCER_LINGER_CLOSE_SECOND': 15
	    }
	    producer = KafkaProducer(configs)
	    producer.close()

def test_pos_5():
	from example.crowdquake.gateway.producer.src.gateway.core.producer import KafkaProducer
	
	def test_pos_5():
	    configs = {
	        'CR_KAFKA_BOOTSTRAP_SERVERS': 'localhost:9092',
	        'CR_KAFKA_LINGER_MS': 20
	    }
	    producer = KafkaProducer(configs)
	    producer.close()