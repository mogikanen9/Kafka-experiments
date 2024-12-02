from confluent_kafka import Consumer, KafkaException, KafkaError

# Configure the consumer
conf = {
    'bootstrap.servers': 'localhost:9092',   # Replace with your Kafka broker
    'group.id': 'my-consumer-group',         # Consumer group ID
    'auto.offset.reset': 'earliest',         # Start consuming from the earliest message
    'enable.auto.commit': True,              # Enable automatic offset commit
    'auto.commit.interval.ms': 1000          # Interval for auto-commit (ms)
}

def main():

    # Create a consumer instance
    consumer = Consumer(conf)

    # Subscribe to a topic
    topic = 'hello-topic'
    consumer.subscribe([topic])

    try:
        while True:
            # Poll for messages (this will block until a message is received)
            msg = consumer.poll(timeout=1.0)

            if msg is None:
                # No message available within the timeout
                continue
            if msg.error():
                # Handle any error
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print(f"End of partition reached: {msg.partition}")
                else:
                    raise KafkaException(msg.error())
            else:
                # Successfully received a message
                print(f"Message received: {msg.value().decode('utf-8')}")

    except KeyboardInterrupt:
        print("Consuming interrupted")
    finally:
        # Close the consumer to commit offsets and clean up
        consumer.close()

if __name__ == "__main__":
    main()
