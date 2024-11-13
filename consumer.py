import threading
import time
import random

class Consumer(threading.Thread):
    def __init__(self, storage, consumer_id, consumption_count):
        super().__init__()
        self.storage = storage
        self.consumer_id = consumer_id
        self.consumption_count = consumption_count

    def run(self):
        for _ in range(self.consumption_count):
            self.storage.consume(self.consumer_id)
            time.sleep(random.uniform(1, 5))