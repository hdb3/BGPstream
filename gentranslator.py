# gentranslator.py

# this is an alternate implmentation which uses generators rather than iterators
# it is derived from the default class in order to ensur that class comparison checks operate as expected

from logger import trace, info, show, warn, error
from framework import Framework
from basemessage import BaseMessage
from source import Source

class GenTranslator(Translator):

    def __init__(self,source):
        Translator.__init__(self)
        self.output_type = type(BaseMessage)
        self.input_type = type(BaseMessage)
        assert issubclass(source,Source)
        assert source.output_type == self.input_type 
        self.next = source
        delattr(self,__next__)
    
    def __iter__(self):
        return self.__gen__()

    def __gen__(self):
        info("start")
        for msg in self.next:
            info("next")
            yield self.translate(msg)
        info("end")

    def translate(self,msg):
        assert issubclass(msg,BaseMessage)
        # do something to the message......
        info("translate")
        return msg
