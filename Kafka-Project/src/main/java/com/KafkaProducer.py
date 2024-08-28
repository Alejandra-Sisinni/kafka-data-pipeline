#Check code
from confluent_kafka import Producer
from confluent_kafka.admin import AdminClient, NewTopicMetadata
from confluent_kafka.errors import CreateTopicsError

# Producer configuration
config = {
    'bootstrap.servers': "localhost:9092",
    'key.serializer': 'org.apache.kafka.common.serialization.StringSerializer',
    'value.serializer': 'org.apache.kafka.common.serialization.StringSerializer',
}

# Create a Kafka producer
producer = Producer(config)

# Check if topic exists (optional)
try:
    admin_client = AdminClient(config)
    topic_metadata = admin_client.list_topics(timeout=5)
    if "kafka.learning.orders" not in topic_metadata.topics:
        # Create the topic if it doesn't exist
        new_topics = [NewTopicMetadata(topic="kafka.learning.orders")]
        result = admin_client.create_topics(new_topics)
        for topic, error in result.items():
            if error:
                print(f"Failed to create topic {topic}: {error}")
except Exception as e:
    print(f"Error checking topic existence: {e}")

# Publish 10 messages with random keys
start_key = random.randint(1000, 9999)
for i in range(start_key, start_key + 10):
    message = f"This is order : {i}"
    # Create a producer record
    producer_record = ProducerRecord("kafka.learning.orders", str(i), message)
    print(f"Sending Message: {producer_record}")

    # Delivery result is handled asynchronously
    future = producer.produce(producer_record, timeout=10)
    try:
        record_metadata = future.get()
        print(f"Produced message to topic {record_metadata.topic()} at offset {record_metadata.offset()}")
    except Exception as e:
        print(f"Failed to deliver message: {e}")

# Flush messages and close producer
producer.poll(0)
producer.flush()