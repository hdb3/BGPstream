
# compose.py

from framework import Framework
from logger import *
from sink import Sink
from source import Source
from translator import Translator

class Compose(Framework):

    def __init__(self):
        Framework.__init__(self)

set_loglevel(SHOW)
