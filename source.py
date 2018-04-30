# source.py

# skeleton source using the default, iterative, style

from logger import trace, info, show, warn, error
#from framework import Framework
from basemessage import BaseMessage

class Source:

    def __init__(self):
        trace()
        pass
    
    def __iter__(self):
        trace()
        return self

    def __next__(self):
        trace()
        if False:
            raise StopIteration
        msg = BaseMessage()
        return msg
