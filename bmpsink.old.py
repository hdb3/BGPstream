# bmpsink.py

from logger import trace, info, show, warn, error
from framework import Framework
from basemessage import WireMessage
from sink import Sink
from bgplib.bmpparse import BMP_message
from bgplib.bmpapp import BmpContext

class BMPSink(Sink):

    def __init__(self,source):
        self.input_type = type(WireMessage)
        #assert issubclass(source,Source)
        #assert source.output_type == self.input_type 
        #self.next = source
        Sink.__init__(self,source)
    
    def run(self):
        info("run starts")
        n = 0
        s = 0
        _max = 0
        _min = None
        context = BmpContext("unknown")
        for msg in self.next:
            assert issubclass(type(msg),WireMessage)
            n += 1
            s += len(msg)
            if len(msg) > _max:
                _max = len(msg)
            if not _min or _min > len(msg):
                _min = len(msg)
            parsed_message = BMP_message(msg)
            context.parse(parsed_message)

        show("%d messages read" % n)
        show("%d bytes read" % s)
        show("%d = average message size" % int(s/n))
        show("%d = minimum message size" % _min)
        show("%d = maximum message size" % _max)
