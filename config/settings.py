import os

from utils.metaclasses import Singleton


class Config(metaclass=Singleton):

    def update_settings(self):
        settings_dict = dict(
            REDIS_HOST=os.environ.get('REDIS_HOST'),
            REDIS_PASSWORD=os.environ.get('REDIS_PASSWORD'),
            USE_CLOUD_EXTENSION=os.environ.get('USE_CLOUD_EXTENSION'),
            REDIS_PORT=os.environ.get('REDIS_PORT'),
            READING_URL=f'{os.environ.get("READING_URL")}?$limit=1'
        )
        return settings_dict
