
import sys
import os
import yaml
from argparse import args_parse

def get_config():

    extra_config = {}
    config = {}

    if len(sys.argv) == 1:
        execpath = os.path.abspath(sys.argv[0])
        configpath = os.path.splitext(execpath)[0] + '.yml'
        if os.path.isfile(configpath):
            sys.stderr.write("using configuration file '%s'" % configpath)
    elif os.path.isfile(sys.argv[1]):
        configpath = sys.argv[1]
        extra_config = args_parse(2)
    else:
        sys.stderr.write("using command line configuration only")
        configpath = None
        extra_config = args_parse(1)

    if configpath:
        ymlfile = open(configpath, 'r')
        config = yaml.load(ymlfile)

    config.update(extra_config)

    return config
