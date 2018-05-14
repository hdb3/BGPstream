# oBMPsink.py

from logger import *
from source import Source
from sink import Sink
from basemessage import WireMessage
import kafka.consumer.fetcher # note this only required to do a type check!!!
from bgplib.oBMPparse import oBMP_parse

class Translator(Sink, Source):

    def __init__(self,source):
        self.input_type = kafka.consumer.fetcher.ConsumerRecord
        self.output_type = WireMessage
        Sink.__init__(self,source)
        Source.__init__(self)
    
    def __next__(self):
        message = next(self.iter)
        assert isinstance(message,kafka.consumer.fetcher.ConsumerRecord)
        return WireMessage(oBMP_parse(bytearray(message.value)))
