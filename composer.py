#!/usr/bin/env python

# composer.py

from framework import Framework
from logger import *
from sink import Sink
from source import Source
#import translator

class Compose(Framework):

    def __init__(self):
        Framework.__init__(self)

    def run(self):
        trace('start')
        source = Source()
        sink = Sink(source)
        sink.run()
        #translator = Translator()
        #sink.bind(translator)
        trace('end')

loglevel=TRACE
Compose().run()
