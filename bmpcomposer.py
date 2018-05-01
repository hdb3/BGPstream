#!/usr/bin/env python

import sys
import yaml
from logger import *
import bmpparser
import tcpsource
import filesource
import wfBMP
import bgpsink
from utils import get_config

config = get_config()

limit = None
if 'limit' in config:
    limit = int(config['limit'])

if config['mode'].upper() == 'FILE':
    source = filesource.Source(config['filename'],limit=limit)
elif config['mode'].upper() == 'ACTIVE':
    source = tcpsource.Source( (config['host'],int(config['port'])),passive=False,limit=limit)
elif config['mode'].upper() == 'PASSIVE':
    source = tcpsource.Source( (config['host'],int(config['port'])),passive=True,limit=limit)
else:
    error("could not determine file/active/passive mode")
    exit()

try:
    translator1 = wfBMP.Translator(source)
    translator2 = bmpparser.Sink(translator1)
    sink = bgpsink.Sink(translator2)
    sink.run()
except KeyboardInterrupt:
    show("exit on keybaord interrupt")

