import json

import redis

from config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, DATASET_NAME, READING_URL
from redis_config.event_hub import EventHubBroker
from utils.metaclasses import Singleton


class RedisBase(metaclass=Singleton):
    def __init__(self):
        self.client = redis.StrictRedis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            password=REDIS_PASSWORD,
            ssl=True
        )
        self.client.set('index', 1)
        self.event_hub = EventHubBroker()

    def connect(self):
        pinging = self.client.ping()
        if not pinging:
            print("Redis availability error")

    def send_data(self, data):
        new_id = self.client.incr('index')
        self.event_hub.send_data(data)

    def set_file_start(self, file):
        self.client.set(file, 'STARTED')
        print(f"Started uploading {file} file")

    def set_file_finished(self, file):
        self.client.set(file, 'COMPLETED')
        print(f"Completed uploading {file}")

    def check_file_available(self, file):
        status = self.client.get(file)
        if status == 'COMPLETED':
            return False
        return True
