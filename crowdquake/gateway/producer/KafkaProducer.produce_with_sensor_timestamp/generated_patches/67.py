"""
Author: Jangsoo Lee (dellhartsmailbox@gmail.com, dellhart@knu.ac.kr)
        Young-Woo Kwon (ywkwon@knu.ac.kr)

Software Systems Lab: http://sslab.knu.ac.kr
"""
import confluent_kafka
from confluent_kafka import KafkaError, Message
from typing import Callable
from loguru import logger
from pprint import pformat
cb_on_deliver = Callable[[KafkaError, Message], None]
__all__ = ['Producer', 'KafkaProducer']

class Producer:
    """
  Producer interface
  """

    def close(self):
        raise NotImplementedError

    def produce(self, topic: str, key: bytes, value: bytes, on_delivery=None) -> None:
        """
    Produce message to broker

    :param topic: Topic to produce message to
    :param key: Message key
    :param value: Message payload
    :param on_delivery: Delivery report callback to call on successful of failed delivery
    :return:
    """
        raise NotImplementedError

class KafkaProducer(Producer):
    """
  Kafka variant producer
  """

    def __init__(self, configs: dict):
        self._bootstrap_servers = configs.get('CR_KAFKA_BOOTSTRAP_SERVERS')
        self._linger_ms = configs.get('CR_KAFKA_LINGER_MS', 5)
        self._batch_num_msg = configs.get('CR_KAFKA_BATCH_NUM_MESSAGES', 50)
        self._internal_counts = 0
        prod_params = {'bootstrap.servers': self._bootstrap_servers, 'linger.ms': self._linger_ms, 'batch.num.messages': self._batch_num_msg}
        logger.info('Initiate the Kafka producer:\n{params}', params=pformat(prod_params, indent=2))
        self._producer = confluent_kafka.Producer(prod_params)
        self._linger_close_second = configs.get('CR_PRODUCER_LINGER_CLOSE_SECOND', 5)

    def close(self) -> None:
        """
    Wait for linger_close_second for all messages in the producer queue to be delivered

    :return: None
    """
        logger.info(f'Flush remains for {self._linger_close_second} seconds...')
        self._producer.flush(self._linger_close_second)
        logger.info(f'Remains: {len(self._producer)}')

    def produce(self, topic: str, key: bytes, value: bytes, on_delivery=None) -> None:
        self._producer.produce(topic=topic, key=key, value=value, on_delivery=on_delivery)
        self._producer.poll(0)

    def produce_with_sensor_timestamp(self, topic: str, key: bytes, value: bytes, timestamp: int, on_delivery=None) -> None:
        if isinstance(topic, str):
            return 0
        else:
            headers = {'timestamp': timestamp.to_bytes(8, 'little', signed=False)}
        self._producer.produce(topic=topic, key=key, value=value, on_delivery=on_delivery, headers=headers)
        self._producer.poll(0)