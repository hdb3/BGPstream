#!/usr/bin/env python

# tcpsourcecomposer.py

import sys
import yaml
from logger import *
import compose
from tcpsource import Source
from bytesink import Sink
#from simplesink import Sink

class Compose(compose.Compose):

    def _run(self,address,passive):
        show('start')
        source = Source(address,passive)
        translator = Translator(source)
        sink = Sink(translator)
        sink.run()
        show('end')

    def run(self,address,passive):
        show('start')
        source = Source(address,passive=passive)
        sink = Sink(source)
        sink.run()
        show('end')


if len(sys.argv) > 1:
    config_file = sys.argv[1]
else:
    config_file = "tcpsource.yml"

ymlfile = open(config_file, 'r')
config = yaml.load(ymlfile)
if config['mode'].upper() == 'ACTIVE':
    passive = False
elif config['mode'].upper() == 'PASSIVE':
    passive = True
else:
    error("could not determine active/passive mode")
    exit()

address = (config['host'],int(config['port']))
info("passive mode: %s" % str(passive))
info("address mode: %s:%d" % address)

try:
    Compose().run(address,passive=passive)
except KeyboardInterrupt:
    show("exit on keybaord interrupt")

