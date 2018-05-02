# basemessage.py

class BaseMessage:
    pass

class ByteStream(BaseMessage):
    pass

class BGPMessage(BaseMessage):
    def __init__(self,tup):
        assert isinstance(tup,tuple) and len(tup) == 3 
        self.msg_type = tup[0]
        self.peer = tup[1]
        self.msg  = tup[2]

class WireMessage(bytearray):
    pass


if __name__ == "__main__":
    bgpMessage = BGPMessage((0,0,bytearray()))
