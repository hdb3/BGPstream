# sink.py

from logger import trace, info, show, warn, error
from framework import Framework
from basemessage import BaseMessage
from source import Source

class Sink(Framework):

    def __init__(self,source):
        Framework.__init__(self)
        self.input_type = type(BaseMessage)
        assert issubclass(type(source),Source)
        assert source.output_type == self.input_type 
        self.next = source
    
    def run(self):
        show("run starts")
        n = 0
        for msg in self.next:
            n += 1
            show("run loop")
        show("run ends - %d cycles" % n)
