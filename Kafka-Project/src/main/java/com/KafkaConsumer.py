#Check code
from confluent_kafka import Consumer

# Consumer configuration
config = {
    'bootstrap.servers': "localhost:9092",
    'key.deserializer': 'org.apache.kafka.common.serialization.StringDeserializer',
    'value.deserializer': 'org.apache.kafka.common.serialization.StringDeserializer',
    'group.id': "kafka-python-consumer",
    'auto.offset.reset': "earliest",
}

# Create a Kafka consumer
consumer = Consumer(config)

# Subscribe to the "kafka.project.orders" topic
consumer.subscribe(["kafka.project.orders"])

# Continuously poll for new messages
while True:
    # Poll with timeout of 100 milliseconds
    messages = consumer.poll(100)

    # Print each message
    for message in messages:
        if message is None:
            continue  # No message received within the timeout
        print(f"Message fetched: {message.key().decode('utf-8')} - {message.value().decode('utf-8')}")

    # Commit offsets periodically (optional)
    consumer.commit(auto_commit=False)

# Close the consumer on exit
consumer.close()