# bmpparser.py

from logger import *
from basemessage import WireMessage, BGPMessage
import sink
import source
from bgplib.bmpparse import BMP_message
from bgplib.bmpapp import BmpContext

class Sink(sink.Sink,source.Source):

    def __init__(self,source):
        self.input_type = WireMessage
        self.output_type = BGPMessage
        sink.Sink.__init__(self,source)
        self.lock = False

    def __iter__(self):
        if self.lock:
            error("this module is not re-entrant")
            exit()
        else:
            self.lock = True
            return self._gen()
    
    #  the module can act as both an endpoint ('sink') and a translator ('sink+source')
    # 'run' method is for usage as a sink
    # this trick is a candidate for pushing into the parent class 'Sink'
    # but that begs question of whther any sinks are really just sinks....


    def run(self):
        n = 0
        for bgp_message in self.__iter__():
            n += 1
        info("%d messages read" % n)

    def _gen(self):
        trace("")
        context = BmpContext("unknown")
        for msg in self.iter:
            assert issubclass(type(msg),WireMessage), "unexpected message type: %s" % str(type(msg))
            parsed_message = BMP_message(msg)
            (msg_type, peer, rmsg) = context.parse(parsed_message)
            if not rmsg is None:
                yield BGPMessage((msg_type, peer, rmsg))

