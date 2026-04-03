import json
from kafka import KafkaProducer
from app.etl import run_etl


def create_producer():
    producer = KafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
    return producer


def send_data():
    producer = create_producer()

    stats = run_etl()

    producer.send("etl-stats", stats)
    producer.flush()

    print("Data sent to Kafka topic 'etl-stats'")


if __name__ == "__main__":
    send_data()