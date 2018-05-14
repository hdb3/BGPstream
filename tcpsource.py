# tcpsource.py
# refer to tcpsource.txt for details

from logger import trace, info, show, warn, error
from basemessage import ByteStream
import source
import tcpsocket

class Source(source.Source):

    def __init__(self,address,passive=True, bufsiz=4096,limit=None):

        self.limit = limit
        self.bufsiz = bufsiz
        self.output_type = ByteStream
        source.Source.__init__(self)
        self.tcpsocket = tcpsocket.Socket(address,passive)
    
    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        trace()
        self.count += 1
        if self.limit is not None and self.limit <= self.count:
            raise StopIteration
        return self.tcpsocket.recv(self.bufsiz)
