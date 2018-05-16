# tcpsource.py
# refer to tcpsource.txt for details

from logger import trace, info, show, warn, error
from basemessage import ByteStream
import tcpsocket

import sink

class Sink(sink.Sink):

    def __init__(self, source, address, passive=True):
        self.input_type = ByteStream
        sink.Sink.__init__(self,source)
        self.tcpsocket = tcpsocket.Socket(address, passive)
    
    def run(self):
        n = 0
        for msg in self.next:
            n += 1
            trace("msg %d" % n)
            self.tcpsocket.send(msg)
            self._next(msg)
        show("%d messages read" % n)
