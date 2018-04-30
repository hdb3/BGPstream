# framework.py

from basemessage import *

from sys import argv,version_info,exit,stderr
from os.path import basename,splitext
import logger
import os

class Framework:

    def __init__(self):
        if version_info < (3,6):
            error("python version >= 3.6 is required")
            exit()

        #env_loglevel = os.environ.get('loglevel')
        #if env_loglevel:
            #logger.set_loglevel(env_loglevel)
            #stderr.write("setting loglevel from environment: [%s]\n" % env_loglevel)
        #else:
            #logger.set_loglevel(logger.SHOW)

    
    def run(self):
        error("framework is not expected to be run")
