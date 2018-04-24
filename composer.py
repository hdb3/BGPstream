#!/usr/bin/env python

# composer.py

from framework import Framework
from logger import *
import sink
import source
#import translator

class Compose(Framework):

    def __init__(self,loglevel):
        Framework.__init__(self,loglevel)

    def run():
        trace('start')
        source = Source()
        sink = Sink(source)
        #translator = Translator()
        sink.bind(translator)
        trace('end')

loglevel = TRACE
Compose(TRACE).run()
