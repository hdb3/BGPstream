# simplesource.py

from logger import trace, info, show, warn, error
from basemessage import ByteStream
import source

class Source(source.Source):

    def __init__(self,fn,bufsiz=4096):
        trace("")
        self.output_type = ByteStream
        source.Source.__init__(self)
        self.fn = fn
        self.bufsiz = bufsiz
    
    def __iter__(self):
        trace("")
        self.file = open(self.fn,'rb')
        return self

    def __next__(self):
        trace("")
        return self.file.read(self.bufsiz)
