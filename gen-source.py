# gen-source.py

from logger import trace, info, show, warn, error
from framework import Framework
from basemessage import BaseMessage

class Source(Framework):

    def __init__(self):
        info("init")
        Framework.__init__(self)
        self.output_type = type(BaseMessage)
    
    def __iter__(self):
        info("iter")
        return self.__gen__()

    def __gen__(self):
        info("start")
        for n in range(4):
            info("next")
            msg = BaseMessage()
            yield msg
