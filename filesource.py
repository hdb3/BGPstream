# simplesource.py

from logger import trace, info, show, warn, error
from framework import Framework
from basemessage import BaseMessage
from source import Source

class FileSource(Source):

    def __init__(self,fn,bufsiz=4096):
        self.output_type = type(BaseMessage)
        Source.__init__(self)
        self.fn = fn
        self.bufsiz = bufsiz
    
    def __iter__(self):
        info("ITER START")
        self.file = open(fn,'rb')
        return self

    def __next__(self):
        return self.read(bufsiz)
