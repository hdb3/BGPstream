#!/usr/bin/env python

# bgpcomposer.py

import sys
from nullsink import NullSink
from wfBMP import BStoBMPwf
from filesource import FileSource
from compose import Compose
from logger import *

class BMPCompose(Compose):

    def run(self,fn):
        show('start')
        source = FileSource(fn)
        translator = BStoBMPwf(source)
        sink = NullSink(translator)
        sink.run()
        show('end')

set_loglevel(SHOW)
BMPCompose().run(sys.argv[1])
