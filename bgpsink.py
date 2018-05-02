
from logger import trace, info, show, warn, error
from basemessage import BGPMessage
import sink
import bgplib.bgpcontext
from bgplib.bgpmsg import BGP_message,BGP_OPEN,BGP_KEEPALIVE,BGP_UPDATE,BGP_NOTIFICATION

class Sink(sink.Sink):

    def __init__(self,source):
        self.input_type = BGPMessage
        sink.Sink.__init__(self,source)
    
    def run(self):
        n = 0
        peers = {}
        for msg in self.iter:
            assert issubclass(type(msg),BGPMessage), "unexpected message type: %s" % str(type(msg))
            n += 1
            bgp_msg = None
            bgp_msg_type = -1
            bmp_msg_type = msg.msg_type
            #trace(str( msg.peer ))
            peer = msg.peer['hash']
            if not peer in peers:
                show("adding new BMP peer context")
                peers[peer] = bgplib.bgpcontext.BGP_context(msg.peer)
                #peers[peer] = bgplib.bgpcontext.new_headless_context()

            if not msg.msg is None:
                bgp_msg = BGP_message(msg.msg)
                peers[peer].consume(msg.msg)
                bgp_msg_type = bgp_msg.bgp_type
            trace("message %d type %d/%d" % (n, bmp_msg_type, bgp_msg_type))

        show("%d messages read" % n)
        for peer in peers.values():
            info(str(peer))
