# nullsink.py

from logger import trace, info, show, warn, error
from framework import Framework
from basemessage import BaseMessage
from sink import Sink

class NullSink(Sink):

    def __init__(self,source):
        self.input_type = BaseMessage
        Sink.__init__(self,source)
    
    def run(self):
        n = 0
        self._start()
        for msg in self.next:
            n += 1
            self._next(msg)
        show("%d messages read" % n)
        self._stop()

    def _start(self):
        pass

    def _stop(self):
        pass

    def _next(self,msg):
        pass
