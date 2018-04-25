# wfBGP.py

from logger import trace, info, show, warn, error
#from framework import Framework
#from basemessage import BaseMessage
from translator import Translator
import struct

class WFtoBGPwf(Translator):

    def __init__(self,source):
        self.output_type = type(WireMessage)
        self.input_type = type(ByteStream)
        Translator.__init__(self,source)
    
    def __iter__(self):
        info("ITER START")
        self.n = 0
        self.iter = iter(self.next)
        return self

    def read(self,count):
        while len(self.buf) < count:
            newbuf = next(self.iter)
            if len(newbuf) == 0:
                raise StopIteration
            self.buf.extend(newbuf)
        rbuf = buf[:count]
        buf = buf[count:]
        return rbuf


    BGP_marker = struct.pack('!QQ',0xffffffffffffffff,0xffffffffffffffff)

    def __next__(self):
        try:
            msg = self.read(18)
            assert msg[0:16] == BGP_marker, "BGP message marker not present"
            bgp_length  = struct.unpack_from('!H', msg, offset=16)[0]
            msg.extend(self.read(bgp_length-18))
            bgp_type    = struct.unpack_from('!B', msg, offset=18)[0]
            assert bgp_type > 0 and bgp_type < 5, "Invalid BGP message type %d" % bgp_type

        except AssertionError as ae:
            error("error parsing the message stream - it makes no sense to continue reading the stream any further after this message" + str(ae))
            raise StopIteration

        except StopIteration:
            info("ITER END (%d cycles)" % self.n)
            raise

        return msg
