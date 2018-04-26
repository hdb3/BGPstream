# bmpsink.py

from logger import trace, info, show, warn, error
from framework import Framework
from basemessage import WireMessage
from nullsink import NullSink
from bgplib.bmpparse import BMP_message
from bgplib.bmpapp import BmpContext

class BMPSink(NullSink):

    def __init__(self,source):
        self.input_type = type(WireMessage)
        #assert issubclass(source,Source)
        #assert source.output_type == self.input_type 
        #self.next = source
        NullSink.__init__(self,source)
    
    def _start(self):
        self.context = BmpContext("unknown")

    def _next(self,msg):
            self.context.parse(BMP_message(msg))

    def _stop(self):
        pass
        # report on the BMP messages processed

