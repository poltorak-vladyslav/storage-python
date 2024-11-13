from queue import Queue
import threading

class Storage:
    def __init__(self, capacity, max_access):
        self.storage = Queue()
        self.items = threading.Semaphore(0)
        self.spaces = threading.Semaphore(capacity)
        self.access_semaphore = threading.Semaphore(max_access)

    def produce(self, producer_id, product):
        self.spaces.acquire()
        self.access_semaphore.acquire()

        self.storage.put(product)
        print(f"Виробник {producer_id} додав {product}")

        self.access_semaphore.release()
        self.items.release()

    def consume(self, consumer_id):
        self.items.acquire()
        self.access_semaphore.acquire()

        product = self.storage.get()
        print(f"Споживач {consumer_id} отримав {product}")

        self.access_semaphore.release()
        self.spaces.release()