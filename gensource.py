# gensource.py

# this is an alternate implmentation which uses generators rather than iterators
# it is derived from the default class in order to ensur that class comparison checks operate as expected

from logger import trace, info, show, warn, error
from framework import Framework
from basemessage import BaseMessage

class GenSource(Source):

    def __init__(self):
        info("init")
        Source.__init__(self)
        self.output_type = type(BaseMessage)
        delattr(self,__next__)
    
    def __iter__(self):
        info("iter")
        return self.__gen__()

    def __gen__(self):
        info("start")
        for n in range(4):
            info("next")
            msg = BaseMessage()
            yield msg
