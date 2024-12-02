import sys
import uuid
from confluent_kafka import Producer

# Configure the producer
conf = {
    "bootstrap.servers": "localhost:9092",  # Replace with your Kafka broker(s)
}


# Delivery callback (optional)
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
        sys.exit(1) 
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def read_payload_sample(fpath):
    with open(fpath, 'r') as file:
        return file.read()

def main():
    print("Let's push some messages")
    # Create a producer instance
    producer = Producer(conf)

    # Publish a message
    topic = "hello-topic"
    key_value = uuid.uuid4().bytes
    message_value = read_payload_sample('request-payload-sample.json')
    producer.produce(topic, key=key_value, value=message_value, callback=delivery_report)

    # Wait for any outstanding messages to be delivered and delivery reports to be received
    producer.flush()

if __name__ == "__main__":
    main()
