# source.bothstyles.py

# this is a reference implementation showing both styles of operation, iterator and generator
# don't use this for anything other than reference!

from logger import trace, info, show, warn, error
from framework import Framework
from basemessage import BaseMessage

class Source(Framework):

    def __init__(self):
        Framework.__init__(self)
        self.output_type = type(BaseMessage)
        self.iterator_style = True
        info("using self.iterator_style = %s" % str(self.iterator_style))
    
    def __iter__(self):
        if self.iterator_style:
            info("ITER START")
            self.n = 0
            return self
        else:
            info("ITER RETURN GEN")
            return self.__gen__()

    def __next__(self):
        info("ITER NEXT")
        if self.n > 3:
            info("ITER END (%d cycles)" % self.n)
            raise StopIteration
        msg = BaseMessage()
        msg.payload = self.n
        show("Out %d" % msg.payload)
        self.n += 1
        return msg

    def __gen__(self):
        info("GEN START")
        for n in range(4):
            info("GEN NEXT")
            msg = BaseMessage()
            msg.payload = n
            show("Out %d" % msg.payload)
            yield msg
        info("GEN END (%d cycles)" % (n+1))
