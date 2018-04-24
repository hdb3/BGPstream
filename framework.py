# framework.py

from basemessage import *

from sys import argv
from os.path import basename,splitext
from logger import trace, info, warn, error

class Framework:

    def __init__(self):
        self.name = splitext(basename(argv[0]))[0]
        trace("__init__")
    
    def run(self):
        error("framework is not expected to be run")
