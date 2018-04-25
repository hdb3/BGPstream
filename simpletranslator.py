# translator.py

from logger import trace, info, show, warn, error
from framework import Framework
from basemessage import BaseMessage
from translator import Translator

class MyTranslator(Translator):

    def __init__(self,source):
        self.output_type = type(BaseMessage)
        self.input_type = type(BaseMessage)
        #assert issubclass(source,Source)
        #assert source.output_type == self.input_type 
        #self.next = source
        Translator.__init__(self,source)
    
    def __iter__(self):
        info("ITER START")
        self.n = 0
        self.iter = iter(self.next)
        return self

    def __next__(self):
        try:
            msg = next(self.iter)
            self.n += 1
            info("ITER NEXT")
            return self.translate(msg)
        except StopIteration:
            info("ITER END (%d cycles)" % self.n)
            raise

    def translate(self,msg):
        assert issubclass(type(msg),BaseMessage)
        show("In %d" % msg.payload)
        if 0 == msg.payload % 2:
            msg.payload = 0-msg.payload
        show("Out %d" % msg.payload)
        return msg
