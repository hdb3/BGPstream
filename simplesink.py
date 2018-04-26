# simple-sink.py

from logger import trace, info, show, warn, error
from framework import Framework
from basemessage import BaseMessage
import sink

class Sink(sink.Sink):

    def __init__(self,source):
        self.input_type = type(BaseMessage)
        #assert issubclass(source,Source)
        #assert source.output_type == self.input_type 
        #self.next = source
        sink.Sink.__init__(self,source)
    
    def run(self):
        info("run starts")
        n = 0
        for msg in self.next:
            show("In %d" % msg.payload)
            n += 1
            trace("process message %d" % n)
        info("run ends - %d cycles" % n)
