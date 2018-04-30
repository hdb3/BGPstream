# simplesource.py

from logger import trace, info, show, warn, error
from basemessage import ByteStream
import sink

class Sink(sink.Sink):

    def __init__(self,fn):
        trace()
        self.input_type = WireMessage
        self.fn = fn
        self.file = open(self.fn,'wb')
        sink.Sink.__init__(self,source)
    
    def run(self):
        trace()
        n = 0
        s = 0
        _max = 0
        _min = None

        for msg in self.iter:
            trace()
            assert issubclass(type(msg),WireMessage), "unexpected message type: %s" % str(type(msg))
            n += 1
            s += len(msg)
            if len(msg) > _max:
                _max = len(msg)
            if not _min or _min > len(msg):
                _min = len(msg)
            self.file.write(msg)

        self.file.close()

        show("%d messages read" % n)
        show("%d bytes read" % s)
        show("%d = average message size" % int(s/n))
        show("%d = minimum message size" % _min)
        show("%d = maximum message size" % _max)
