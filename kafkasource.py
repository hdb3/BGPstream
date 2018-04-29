# kafkasource.py

import yaml
from kafka import KafkaConsumer
import kafka.consumer.fetcher
from kafka.errors import NoBrokersAvailable
from logger import stack_trace, trace, info, show, warn, error
from framework import Framework
from basemessage import BaseMessage
from source import Source

class KafkaSource(Source):

    def __init__(self,topic,bootstrap_servers,client_id):
        self.output_type = kafka.consumer.fetcher.ConsumerRecord
        Source.__init__(self)
        self.topic = topic
        self.bootstrap_servers = bootstrap_servers
        self.client_id = client_id
    
    def __iter__(self):
        while True:
            try:
                self.consumer=KafkaConsumer( self.topic,
                                             api_version_auto_timeout_ms = 1000,
                                             request_timeout_ms = 1000,
                                             bootstrap_servers=self.bootstrap_servers,
                                             client_id=self.client_id)
                break
            except NoBrokersAvailable:
                show("retrying connection to Kafka broker")

        show("connected to Kafka broker at %s" % self.bootstrap_servers)

        return self.__gen__()

    def __gen__(self):
        for message in self.consumer:
            yield message
        self.consumer.close()
