# framework.py

from basemessage import *

from sys import argv,version_info,exit
from os.path import basename,splitext
from logger import trace, info, warn, error

class Framework:

    def __init__(self):
        if version_info < (3,6):
            error("python version >= 3.6 is required")
            exit()
    
    def run(self):
        error("framework is not expected to be run")
