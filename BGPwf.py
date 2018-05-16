# BGPwf.py
#
# convert BGP messages from the bmpparser back into simple wireformat

import struct
from logger import *
from basemessage import ByteStream, BGPMessage
from source import Source

class Translator(Source):

    def __init__(self,source):
        self.output_type = ByteStream
        self.input_type = BGPMessage
        assert self.input_type == source.output_type
        self.iter = iter(source)
    
    def __iter__(self):
        return self

    def __next__(self):
        bgp_message = next(self.iter)
        return WireMessage(bgp_message[2])
