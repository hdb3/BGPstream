# source.py

from logger import trace, info, warn, error
from framework import Framework
from basemessage import BaseMessage

class Source(Framework):

    def __init__(self):
        trace("0")
        Framework.__init__(self)
        self.output_type = type(BaseMessage)
    
    def __iter__(self):
        trace("1")
        self.n = 0
        return self
        #return self.__gen__()

    def __next__(self):
        trace("2")
        if self.n > 5:
            raise StopIteration
        msg = BaseMessage()
        msg.payload = self.n
        self.n += 1
        trace("generate message %d" % self.n)

    def __gen__(self):
        trace("3")
        print("__iter__")
        info("run starts")
        for n in range(5):
            trace("4")
            msg = BaseMessage()
            msg.payload = n
            yield(msg)
        info("run ends - %d cycles" % n)
