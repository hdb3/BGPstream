#!/usr/bin/env python

# kafkacomposer.py

import sys
import yaml
from oBMPsink import OSink
from kafkasource import KafkaSource
import compose
from logger import *

class Compose(compose.Compose):

    def run(self,topic,bootstrap_servers,client_id):
        show('start')
        source = KafkaSource(topic,bootstrap_servers,client_id)
        #translator = BStoBMPwf(source)
        OSink(source).run()
        show('end')


if len(sys.argv) > 1:
    config_file = sys.argv[1]
else:
    config_file = "kafkacomposer.yml"

ymlfile = open(config_file, 'r')
config = yaml.load(ymlfile)

try:
    Compose().run(config['topic'],
                   config['bootstrap_servers'],
                   config['client_id'])
except KeyboardInterrupt:
    print("exit on keybaord interrupt")

