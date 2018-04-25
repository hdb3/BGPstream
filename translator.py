# translator.py

from logger import trace, info, warn, error
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
        self.iterator_style = True
        info("using self.iterator_style = True")
    
    def __iter__(self):
        if self.iterator_style:
            info("iterator run starts")
            self.n = 0
            self.next = iter(self.next)
            return self
        else:
            return self.__gen__()

    def __next__(self):
        try:
            trace("")
            #return self.translate(next(self.next))
            return self.translate(self.next)
            self.n += 1
        except StopIteration:
            info("iterator run ends - %d cycles" % n)
            raise

    def __gen__(self):
        info("generator run starts")
        for msg in self.next():
            trace("")
            yield self.translate(self.next)
        info("generator run ends - %d cycles" % n)

    def translate(self,msg):
        info("type msg is %s" % str(type(msg)))
        assert isinstance(msg,BaseMessage)
        if 0 == msg.payload % 2:
            msg.payload = 0-msg.payload
        return msg
