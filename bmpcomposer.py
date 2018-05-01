#!/usr/bin/env python


import sys
import yaml
from logger import *
import bmpparser
import tcpsource
import filesource
import wfBMP


def get_config(fn):

    if len(sys.argv) > 1:
        config_file = sys.argv[1]
    else:
        config_file = fn

    ymlfile = open(config_file, 'r')
    return yaml.load(ymlfile)

config = get_config("bmpcomposer.yml")

# tcpsourcecomposer.py

if config['mode'].upper() == 'FILE':
    source = filesource.Source(config['filename'])
    translator = wfBMP.Translator(source)
    sink = bmpparser.Sink(translator)
elif config['mode'].upper() == 'ACTIVE':
    source = tcpsource.Source( (config['host'],int(config['port'])),passive=False)
    sink = bmpparser.Sink(source)
elif config['mode'].upper() == 'PASSIVE':
    source = tcpsource.Source( (config['host'],int(config['port'])),passive=True)
    sink = bmpparser.Sink(source)
else:
    error("could not determine file/active/passive mode")
    exit()


try:
    sink.run()
except KeyboardInterrupt:
    show("exit on keybaord interrupt")

