from config import Config

config = Config()
settings = config.update_settings()

REDIS_PORT = settings['REDIS_PORT']
REDIS_HOST = settings['REDIS_HOST']
READING_URL = settings.get('READING_URL')
REDIS_PASSWORD = settings.get('REDIS_PASSWORD')
USE_CLOUD_EXTENSION = settings.get('USE_CLOUD_EXTENSION')
DATASET_NAME = 'Stock Market'
