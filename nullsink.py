# nullsink.py

from logger import *
from basemessage import BaseMessage
import sink

class Sink(sink.Sink):

    def __init__(self,source):
        self.input_type = BaseMessage
        sink.Sink.__init__(self,source)
    
    def run(self):
        n = 0
        self._start()
        for msg in self.next:
            n += 1
            trace("msg %d" % n)
            self._next(msg)
        show("%d messages read" % n)
        self._stop()

    def _start(self):
        pass

    def _stop(self):
        pass

    def _next(self,msg):
        pass
