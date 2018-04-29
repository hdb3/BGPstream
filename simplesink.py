# simple-sink.py

from logger import trace, info, show, warn, error
from framework import Framework
from basemessage import BaseMessage
import sink

class Sink(Framework):

    def __init__(self,source):

        ### self.input_type = type(BaseMessage)
        ### assert issubclass(type(source),Source)
        ### assert source.output_type == self.input_type
        # typically a specific Sink implementation could call sink.Sink.__init__() rather than do these checks itself...
        ### sink.Sink.__init__(self,source)

        # but only this line is essential
        self.next = source

    
    def run(self):
        show("run starts")
        n = 0
        for msg in self.next:
            show("message received, type %s" % str(type(msg)))
            n += 1
            trace("process message %d" % n)
        show("run ends - %d cycles" % n)
