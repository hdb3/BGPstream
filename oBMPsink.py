# oBMPsink.py

from logger import trace, info, show, warn, error
from framework import Framework
import kafka.consumer.fetcher
import nullsink
from bgplib.oBMPparse import oBMP_parse

class OSink(nullsink.NullSink):

    def __init__(self,source):
        self.input_type = kafka.consumer.fetcher.ConsumerRecord
        #assert issubclass(source,Source)
        #assert source.output_type == self.input_type 
        #self.next = source
        nullsink.NullSink.__init__(self,source)
    
    def _next(self,message):
        bmp_msg = oBMP_parse(bytearray(message.value))
