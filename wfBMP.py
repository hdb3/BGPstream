# wfBMP.py

from logger import trace, info, show, warn, error
#from framework import Framework
from basemessage import WireMessage, ByteStream
from translator import Translator
import struct

class BStoBMPwf(Translator):

    def __init__(self,source):
        self.output_type = type(WireMessage)
        self.input_type = type(ByteStream)
        Translator.__init__(self,source)
    
    def __iter__(self):
        info("ITER START")
        self.n = 0
        self.buf = bytearray()
        self.iter = iter(self.next)
        return self

    def read(self,count):
        while len(self.buf) < count:
            newbuf = next(self.iter)
            if len(newbuf) == 0:
                raise StopIteration
            self.buf.extend(newbuf)
        rbuf = self.buf[:count]
        self.buf = self.buf[count:]
        return rbuf

    def __next__(self):
        try:
            msg = self.read(6)
            version  = struct.unpack_from('!B', msg, offset=0)[0]
            length   = struct.unpack_from('!I', msg, offset=1)[0]
            msg_type = struct.unpack_from('!B', msg, offset=5)[0]
            msg.extend(self.read(length-6))
            assert 3 == version, "failed version check, expected 3 got %x" % version
            assert msg_type < 7, "failed message type check, expected < 7, got %x" % msg_type


        except AssertionError as ae:
            error("error parsing the message stream - it makes no sense to continue reading the stream any further after this message" + str(ae))
            raise StopIteration

        except StopIteration:
            info("ITER END (%d cycles)" % self.n)
            raise

        return WireMessage(msg)
