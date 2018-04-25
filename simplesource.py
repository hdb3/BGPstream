# simplesource.py

from logger import trace, info, show, warn, error
from framework import Framework
from basemessage import BaseMessage
from source import Source

class MySource(Source):

    def __init__(self):
        self.output_type = type(BaseMessage)
        Source.__init__(self)
    
    def __iter__(self):
        info("ITER START")
        self.n = 0
        return self

    def __next__(self):
        info("ITER NEXT")
        if self.n > 3:
            info("ITER END (%d cycles)" % self.n)
            raise StopIteration
        msg = BaseMessage()
        msg.payload = self.n
        self.n += 1
        return msg
