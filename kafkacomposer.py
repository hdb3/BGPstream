#!/usr/bin/env python

# kafkacomposer.py

import sys
import yaml
import oBMPtoBMP
import bmpparser
import kafkasource
from logger import *
from utils import get_config

config = get_config()

source = kafkasource.Source(config['topic'],config['bootstrap_servers'],config['client_id'])
translator = oBMPtoBMP.Translator(source)
sink = bmpparser.Sink(translator)

try:
    sink.run()
except KeyboardInterrupt:
    print("exit on keybaord interrupt")
