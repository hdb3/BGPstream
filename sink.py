# sink.py

from logger import trace, info, warn, error
from framework import Framework
from basemessage import BaseMessage
from source import Source

class Sink(Framework):

    def __init__(self,source):
        Framework.__init__(self)
        self.input_type = type(BaseMessage)
        assert isinstance(source,Source)
        assert source.output_type == self.input_type 
        self.next = source
    
    def run(self):
        info("run starts")
        n = 0
        for msg in self.next:
            n += 1
            print("process message %d" % n)
            trace("process message %d" % n)
        info("run ends - %d cycles" % n)
