
from logger import trace, info, show, warn, error
from basemessage import WireMessage
import sink
import bgplib.bgpcontext
from bgplib.bgpmsg import BGP_message,BGP_OPEN,BGP_KEEPALIVE,BGP_UPDATE,BGP_NOTIFICATION

class Sink(sink.Sink):

    def __init__(self,source):
        self.input_type = WireMessage
        sink.Sink.__init__(self,source)
    
    def run(self):
        n = 0
        context = bgplib.bgpcontext.new_headless_context()
        for msg in self.iter:
            assert issubclass(type(msg),WireMessage), "unexpected message type: %s" % str(type(msg))
            n += 1
            bgp_msg = BGP_message(msg)
            msg_type = bgp_msg.bgp_type
            trace("message %d type %d" % (n, msg_type))
            #context.consume(msg)

        show("%d messages read" % n)
