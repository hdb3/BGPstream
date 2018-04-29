#!/usr/bin/env python

# simple-composer.py

#from framework import Framework
from simplesink import Sink
from simpletranslator import MyTranslator
from simplesource import MySource
from kafkasource import KafkaSource
from compose import Compose
from logger import *
import inspect

class MyCompose(Compose):

    def __init__(self):
        Compose.__init__(self)

    def run1(self):
        show('start')
        source = MySource()
        sink = Sink(source)
        sink.run()
        show('end')

    def run2(self):
        show('start')
        source = MySource()
        translator = MyTranslator(source)
        sink = MySink(translator)
        sink.run()
        show('end')

set_loglevel(TRACE)
MyCompose().run1()
