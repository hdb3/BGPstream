#!/usr/bin/env python

# composer.py

from framework import Framework
from logger import *
from sink import Sink
from source import Source
from translator import Translator

class Compose(Framework):

    def __init__(self):
        Framework.__init__(self)

    def run1(self):
        trace('start')
        source = Source()
        sink = Sink(source)
        sink.run()
        trace('end')

    def run2(self):
        trace('start')
        source = Source()
        translator = Translator(source)
        sink = Sink(translator)
        #exit()
        sink.run()
        trace('end')

loglevel=TRACE
Compose().run2()
