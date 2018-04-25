# translator.py

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
        self.iterator_style = True
        info("using self.iterator_style = %s" % str(self.iterator_style))
    
    def __iter__(self):
        if self.iterator_style:
            info("ITER START")
            self.n = 0
            self.iter = iter(self.next)
            return self
        else:
            info("ITER RETURN GEN")
            return self.__gen__()

    def __next__(self):
        try:
            msg = next(self.iter)
            self.n += 1
            info("ITER NEXT")
            return self.translate(msg)
        except StopIteration:
            info("ITER END (%d cycles)" % self.n)
            raise

    def __gen__(self):
        info("GEN START")
        n = 0
        for msg in self.next:
            n += 1
            yield self.translate(msg)
        info("GEN END (%d cycles)" % n)

    def translate(self,msg):
        assert isinstance(msg,BaseMessage)
        show("In %d" % msg.payload)
        if 0 == msg.payload % 2:
            msg.payload = 0-msg.payload
        show("Out %d" % msg.payload)
        return msg
