# source.py

from logger import trace, info, warn, error
from framework import Framework

class Source(Framework):

    def __init__():
        Framework.__init__(self)
        self.output_type = type(BaseMessage)
    
    def next():
        info("run starts")
        for n in range(10):
            msg = BaseMessage()
            msg.payload = n
            trace("generate message %d" % n)
            yield(msg)
        info("run ends - %d cycles" % n)
