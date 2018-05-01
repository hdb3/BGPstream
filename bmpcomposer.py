#!/usr/bin/env python


import sys
import yaml
from logger import *
import bmpparser
import tcpsource
import filesource
import wfBMP
from argparse import args_parse
from utils import get_config


#from os.path import basename,splitext

def ____get_config():

    extra_config = {}
    config = {}

    if len(sys.argv) == 1:
        execpath = os.path.abspath(sys.argv[0])
        configpath = os.path.splitext(execpath)[0] + '.yml'
        if os.path.isfile(configpath):
            warn("using configuration file '%s'" % configpath)
    elif os.path.isfile(sys.argv[1]):
        configpath = sys.argv[1]
        extra_config = args_parse(2)
    else:
        info("using command line configuration only")
        configpath = None
        extra_config = args_parse(1)

    if configpath:
        ymlfile = open(configpath, 'r')
        config = yaml.load(ymlfile)

    config.update(extra_config)

    return config


config = get_config()
print(config)

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
    translator = wfBMP.Translator(source)
    sink = bmpparser.Sink(translator)
    sink.run()
except KeyboardInterrupt:
    show("exit on keybaord interrupt")

