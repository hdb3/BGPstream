# sink.py

class Sink:
from sys import argv
from os.path import basename,splitext
from logger import trace, info, warn, error

def __init__(source):
    self.input_type = type(MyInputMessage)
    assert isinstance(source,Source)
    assert source.output_type == self.input_type 
    self.next = source.next
    self.name = splitext(basename(argv[0]))[0]
    
def run():
    info("run starts")
    for msg in self.next:
        trace("process message %d" % n)
    info("run ends")
