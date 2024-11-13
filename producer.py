import threading
import time
import random

from product import Product

class Producer(threading.Thread):
    def __init__(self, storage, producer_id, production_count):
        super().__init__()
        self.storage = storage
        self.producer_id = producer_id
        self.production_count = production_count

    def run(self):
        for i in range(self.production_count):
            product = Product(i)
            self.storage.produce(self.producer_id, product)
            time.sleep(random.uniform(1, 5))