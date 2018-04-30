# bytesink.py

from logger import trace, info, show, warn, error
from basemessage import WireMessage
from nullsink import NullSink

class Sink:

    def __init__(self,source):
        self.input_type = WireMessage
        self.iter = source

    def run(self):
        trace("")
        n = 0
        s = 0
        _max = 0
        _min = None

        for msg in self.iter:
            if n == 0:
                info("message type = %s" % str(type(msg)))
            n += 1
            s += len(msg)
            if len(msg) > _max:
                _max = len(msg)
            if not _min or _min > len(msg):
                _min = len(msg)

        show("%d messages read" % n)
        show("%d bytes read" % s)
        show("%d = average message size" % int(s/n))
        show("%d = minimum message size" % _min)
        show("%d = maximum message size" % _max)
