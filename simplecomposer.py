#!/usr/bin/env python

# simple-composer.py

#from framework import Framework
#from logger import *
from simplesink import MySink
from simpletranslator import MyTranslator
from simplesource import MySource
from compose import Compose
from logger import *
import inspect


def classlookup(cls):
    c = list(cls.__bases__)
    for base in c:
        c.extend(classlookup(base))
    return c

class MyCompose(Compose):

    def __init__(self):
        Compose.__init__(self)

    def run1(self):
        show('start')
        source = MySource()
        sink = MySink(source)
        sink.run()
        show('end')

    def run2(self):
        show('start')
        source = MySource()
        translator = MyTranslator(source)
        sink = MySink(translator)
        sink.run()
        show('end')

set_loglevel(SHOW)
MyCompose().run2()
