from confluent_kafka import Producer, Consumer, KafkaException

class KafkaManager:
    def __init__(self, kafka_config):
        self.producer = Producer(kafka_config)
        self.consumer = Consumer(kafka_config)

    def produce(self, topic, message):
        try:
            self.producer.produce(topic, message)
            self.producer.flush()
        except KafkaException as e:
            print(f"Failed to send message: {e}")

    def consume(self, topic):
        self.consumer.subscribe([topic])
        try:
            msg = self.consumer.poll(1.0)
            if msg is None:
                return None
            if msg.error():
                raise KafkaException(msg.error())
            else:
                return msg.value().decode('utf-8')
        except KafkaException as e:
            print(f"Failed to consume message: {e}")
