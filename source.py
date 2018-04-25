# source.py

# skeleton source using the default, iterative, style

from logger import trace, info, show, warn, error
from framework import Framework
from basemessage import BaseMessage

class Source(Framework):

    def __init__(self):
        Framework.__init__(self)
        self.output_type = type(BaseMessage)
    
    def __iter__(self):
        return self

    def __next__(self):
        if False:
            raise StopIteration
        msg = BaseMessage()
        return msg
