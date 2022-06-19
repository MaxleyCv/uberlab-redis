import requests

from config import READING_URL
from utils.metaclasses import Singleton


class DataReader(metaclass=Singleton):
    def __init__(self):
        self.offset = 0

    def read_all(self, result = True):
        while result:
            r = self.read_next()
            if r.status_code != 200:
                raise Exception('Error fetching')
            result = r.json()
            if result:
                yield result
        self.offset = 0

    def read_next(self):
        url = f'{READING_URL}&&offset={self.offset}'
        self.offset += 1
        return requests.get(url)
