from consumer import Consumer
from producer import Producer
from storage import Storage

def main():
    capacity = 5
    doors = 2
    producer_count = 3
    consumer_count = 3
    items_per_producer = 5
    items_per_consumer = 5

    storage = Storage(capacity, doors)

    producers = []
    for i in range(producer_count):
        producer = Producer(storage, i, items_per_producer)
        producer.start()
        producers.append(producer)

    consumers = []
    for i in range(consumer_count):
        consumer = Consumer(storage, i, items_per_consumer)
        consumer.start()
        consumers.append(consumer)

    for producer in producers:
        producer.join()

    for consumer in consumers:
        consumer.join()


if __name__ == "__main__":
    main()