# filesource.py

from logger import *
from basemessage import ByteStream
import source

class Source(source.Source):

    def __init__(self,fn,bufsiz=4096,limit=None):
        trace("")
        self.limit = limit
        self.output_type = ByteStream
        source.Source.__init__(self)
        self.fn = fn
        self.bufsiz = bufsiz
    
    def __iter__(self):
        trace("")
        self.count = 0
        self.file = open(self.fn,'rb')
        return self

    def __next__(self):
        self.count += 1
        if self.limit is not None and self.limit <= self.count:
            raise StopIteration
        return self.file.read(self.bufsiz)
