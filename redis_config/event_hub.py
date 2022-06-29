import json

from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

from config import EVENT_HUB_CONNECTION, EVENT_HUB_NAME
from utils.metaclasses import Singleton


class EventHubBroker(metaclass=Singleton):

    def __init__(self):
        self.producer = EventHubProducerClient.from_connection_string(
            conn_str=EVENT_HUB_CONNECTION,
            eventhub_name=EVENT_HUB_NAME
        )

    def send_data(self, data):
        async with self.producer:
            event_data_batch = await self.producer.create_batch()

            event_data_batch.add(EventData(json.dumps(data)))

            await self.producer.send_batch(event_data_batch)
