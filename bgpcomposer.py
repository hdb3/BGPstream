#!/usr/bin/env python

# bgpcomposer.py

from bgpsink import BGPSink
from wfBGP import WFtoBGPwf
from filesource import FileSource
from compose import Compose
from logger import *

class BGPCompose(Compose):

    def run(self):
        show('start')
        source = FileSource(fn)
        translator = WFtoBGPwf(source)
        sink = BGPSink(translator)
        sink.run()
        show('end')

set_loglevel(SHOW)
BGPCompose().run()
