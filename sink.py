# sink.py

class Sink:

def __init__(source):
    self.input_type = type(MyInputMessage)
    assert isinstance(source,Source)
    assert source.output_type == self.input_type 
    self.next = source.next

def run():
    trace("run starts")
    for msg in self.next:
        trace("process message %d" % n)
    trace("run ends")
