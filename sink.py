# sink.py

from logger import *
from basemessage import BaseMessage
from source import Source

class Sink:

    def __init__(self,source):
        trace("source %s providing message type %s, expecting message type %s" % (str(type(source)), str(source.output_type), str(self.input_type)))
        assert issubclass(type(source),Source), "source class is %s" % str(type(source))
        assert source.output_type == self.input_type , "incompatible types- source:%s/expected:%s" % (str(source.output_type), str(self.input_type))
        self.source = source
        self.iter = iter(source)
    
    def run(self):
        show("run starts")
        n = 0
        for msg in self.iter:
            n += 1
            trace("msg %d" % n))
        show("run ends - %d cycles" % n)
