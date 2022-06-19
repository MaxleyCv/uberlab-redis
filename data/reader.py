from sodapy import Socrata
import pandas as pd

from config import READING_URL
from utils.metaclasses import Singleton


class DataReader(metaclass=Singleton):
    def __init__(self):
        self.offset = 0
        self.client = Socrata("www.dallasopendata.com", None)

    def read_all(self, result=True):
        while len(result):
            result = self.read_next().values
            for r1 in result:
                yield r1
        self.offset = 0

    def read_next(self):
        res = self.client.get(READING_URL, limit=2000, offset=self.offset)
        self.offset += 2000
        return pd.DataFrame.from_records(res)
