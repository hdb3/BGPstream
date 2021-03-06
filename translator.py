# ranslator.py
# skeleton source using the default, iterative, style

from logger import trace, info, show, warn, error
from framework import Framework
from basemessage import BaseMessage
from source import Source

class Translator(Source):

    def __init__(self,source):

        info("init")
        Framework.__init__(self)
        self.output_type = type(BaseMessage)
        self.input_type = type(BaseMessage)
        assert issubclass(type(source),Source)
        assert source.output_type == self.input_type 
        self.next = source
    
    def __iter__(self):
        self.iter = iter(self.next)
        return self

    def __next__(self):
        try:
            msg = next(self.iter)
            return self.translate(msg)
        except StopIteration:
            info("stop")
            raise

    def translate(self,msg):
        assert issubclass(type(msg),BaseMessage)
        # do something to the message......
        info("translate")
        return msg



