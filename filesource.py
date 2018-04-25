# simplesource.py

from logger import trace, info, show, warn, error
from framework import Framework
from basemessage import ByteStream
from source import Source

class FileSource(Source):

    def __init__(self,fn,bufsiz=4096):
        self.output_type = type(ByteStream)
        Source.__init__(self)
        self.fn = fn
        self.bufsiz = bufsiz
    
    def __iter__(self):
        info("ITER START")
        self.file = open(self.fn,'rb')
        return self

    def __next__(self):
        return self.file.read(self.bufsiz)
