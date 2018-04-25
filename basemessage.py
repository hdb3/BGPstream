# basemessage.py

# potentially could just put this in the framework file

class BaseMessage:
    pass

class ByteStream(BaseMessage):
    pass

class WireMessage(bytearray):
    pass
