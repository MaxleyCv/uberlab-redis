from config import Config, READING_URL
from data import DataReader
from operators import DataWriter, RedisWriterStrategy, ConsoleWriterStrategy
from redis_config import RedisBase


class DataController:
    def __init__(self):
        config = Config()
        settings = config.update_settings()
        if settings['USE_CLOUD_EXTENSION']:
            self.writer: DataWriter = RedisWriterStrategy()
        else:
            self.writer: DataWriter = ConsoleWriterStrategy()

    def start_populating(self):
        reader = DataReader()
        redis_base = RedisBase()
        if redis_base.check_file_available(READING_URL):
            print(f"Started populating {READING_URL}")
            for response in reader.read_all():
                self.writer.send(response)
            redis_base.set_file_finished(READING_URL)
            print('File status finished')
        else:
            print('This file was completed')
        return 'Success'
