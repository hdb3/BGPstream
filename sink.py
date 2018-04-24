# sink.py

from logger import trace, info, warn, error
from framework import Framework

class Sink(Framework):

    def __init__(source):
        Framework.__init__(self)
        self.input_type = type(BaseMessage)
        assert isinstance(source,Source)
        assert source.output_type == self.input_type 
        self.next = source.next
    
    def run():
        info("run starts")
        n = 0
        for msg in self.next:
            n += 1
            trace("process message %d" % n)
        info("run ends - %d cycles" % n)
