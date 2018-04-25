# gentranslator.py

from logger import trace, info, show, warn, error
from framework import Framework
from basemessage import BaseMessage
from source import Source

class Translator(Source):

    def __init__(self,source):
        Framework.__init__(self)
        self.output_type = type(BaseMessage)
        self.input_type = type(BaseMessage)
        assert isinstance(source,Source)
        assert source.output_type == self.input_type 
        self.next = source
    
    def __iter__(self):
        return self.__gen__()

    def __gen__(self):
        info("start")
        for msg in self.next:
            info("next")
            yield self.translate(msg)
        info("end")

    def translate(self,msg):
        assert isinstance(msg,BaseMessage)
        # do something to the message......
        info("translate")
        return msg
