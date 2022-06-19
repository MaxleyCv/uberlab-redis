from config import READING_URL
from redis_config import RedisBase


class DataWriter:
    def send(self, data):
        pass


class ConsoleWriterStrategy(DataWriter):
    def send(self, data):
        print(data)


class RedisWriterStrategy(DataWriter):
    def send(self, data):
        redis_base = RedisBase()
        redis_base.send_data(data)
