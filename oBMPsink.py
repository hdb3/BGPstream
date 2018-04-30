# oBMPsink.py

from logger import stack_trace, trace, info, show, warn, error
from framework import Framework
import kafka.consumer.fetcher
import nullsink
from bgplib.oBMPparse import oBMP_parse

class OSink(nullsink.NullSink):

    def __init__(self,source):
        self.input_type = kafka.consumer.fetcher.ConsumerRecord
        nullsink.NullSink.__init__(self,source)
    
    def _next(self,message):
        assert isinstance(message,kafka.consumer.fetcher.ConsumerRecord)
        trace("kafka message received")
        bmp_msg = oBMP_parse(bytearray(message.value))
        info("type of BMP message %s" % str(type(bmp_msg)))
