#!/usr/bin/env python

# tcpsourcecomposer.py

import sys
import yaml
print(globals())
from logger import *
#from logger import info
#print("loglevel1", loglevel)
#print(globals())
#exit()
#logger_init()
#import compose
#from tcpsource import Source
#from simplesink import Sink

print("loglevel", loglevel)
trace("trace")
print("1")
info("info")
print("2")
show("show")
print("3")
warn("warn")
print("4")
error("error")
print("5")
exit()
set_loglevel(TRACE)
trace("trace")
info("info")
show("show")
warn("warn")
error("error")


print("loglevel", loglevel)
if len(sys.argv) > 1:
    config_file = sys.argv[1]
else:
    config_file = "tcpsource.yml"

ymlfile = open(config_file, 'r')
config = yaml.load(ymlfile)
if config['mode'].upper() == 'ACTIVE':
    passive = False
elif config['mode'].upper() == 'PASSIVE':
    passive = True
else:
    error("could not determine active/passive mode")
    exit()

address = (config['host'],int(config['port']))
print("loglevel", loglevel)
info("passive mode: %s" % str(passive))
info("address mode: %s:%d" % address)
exit()

try:
    Compose().run(address,passive)
except KeyboardInterrupt:
    show("exit on keybaord interrupt")

