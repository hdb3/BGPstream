# source.py

from logger import trace, info, warn, error
from framework import Framework
from basemessage import BaseMessage

class Source(Framework):

    def __init__(self):
        Framework.__init__(self)
        self.output_type = type(BaseMessage)
    
    def __iter__(self):
        print("__iter__")
        return self.__gen__()

    def __next__(self):
        info("run starts")
        for n in range(10):
            msg = BaseMessage()
            msg.payload = n
            trace("generate message %d" % n)
            yield(msg)
        info("run ends - %d cycles" % n)

    def __gen__(self):
        print("__iter__")
        info("run starts")
        for n in range(10):
            msg = BaseMessage()
            msg.payload = n
            trace("generate message %d" % n)
            yield(msg)
        info("run ends - %d cycles" % n)
