# poc-kafka-experiments
Misc experiments how to work with Kafka

## docker-compose.yaml
  - kafka+zookeeper
  - kdrop UI


How to run? `docker-compose  -f .\docker-compose.yml up`

## docker-compose-rest-proxy.yaml
  - kafka+zookeeper
  - kdrop UI
  - kafka-rest-proxy

How to run? `docker-compose  -f .\docker-compose-rest-proxy.yaml up`

## Important!
To make 'kafka:9092' reachable - update hosts file with `127.0.0.1 kafka`

## rest-proxy
 - curl sample on how to push messages to topic
 - curl sample on how to list topic

## Python (folder python)
 - Install Python 3.12 or higher
 - Install required packages `pip install -r requirements.txt`
