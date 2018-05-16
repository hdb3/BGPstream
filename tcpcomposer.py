#!/usr/bin/env python

import sys
import yaml
from logger import *
import bmpparser
import tcpsource
import filesource
import wfBMP
import BGPwf
import tcpsink
from utils import get_config

config = get_config()

source_config = config['source']
source_mode = source_config['mode'].upper()

sink_config = config['sink']
sink_mode = sink_config['mode'].upper()
if sink_mode== 'ACTIVE':
    sink_passive = False 
else:
    sink_passive = True

limit = None
if 'limit' in config:
    limit = int(config['limit'])

if source_mode== 'FILE':
    filename = source_config['filename']
    source = filesource.Source(filename,limit=limit)
elif source_mode in ( 'ACTIVE','PASSIVE'):
    address = (source_config['host'],int(source_config['port']))
    if source_mode == 'ACTIVE':
        source_passive = False 
    else:
        source_passive = True
    source = tcpsource.Source(address, source_passive, limit=limit)
else:
    error("could not determine source file/active/passive mode")
    exit()

if sink_mode== 'FILE':
    filename = sink_config['filename']
    sink = filesink.Source(filename,limit=limit)
elif sink_mode in ( 'ACTIVE','PASSIVE'):
    address = (sink_config['host'],int(sink_config['port']))
    if sink_mode == 'ACTIVE':
        sink_passive = False 
    else:
        sink_passive = True
    _sink = lambda source : tcpsink.Sink(source, address, sink_passive)
else:
    error("could not determine sink file/active/passive mode")
    exit()

try:
    translator1 = wfBMP.Translator(source)
    translator2 = bmpparser.Sink(translator1)
    translator3 = BGPwf.Translator(translator2)
    sink = _sink(translator3)
    sink.run()
except KeyboardInterrupt:
    show("exit on keybaord interrupt")

