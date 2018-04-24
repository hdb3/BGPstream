import datetime
import sys
from traceback import extract_stack
from os.path import splitext

TRACE = 4
INFO  = 3
WARN  = 2
ERROR = 1
NONE  = 0

loglevel = NONE 
logfile = sys.stderr

def __write(s,l):
    frame = extract_stack(limit=1)[0][0]
    frame = splitext(frame)[0]
    global logfile
    ts = datetime.datetime.now().strftime("%x %X")
    logfile.write("%s [%s] %s -- %s" % (ts, frame.ljust(8),l, s))
          
def trace(s):
    global loglevel
    if loglevel >= TRACE:
            __write(s,'TRACE')
                            
def info(s):
    global loglevel
    if loglevel >= INFO:
            __write(s,'INFO ')
                            
def warn(s):
    global loglevel
    if loglevel >= WARN:
            __write(s,'WARN ')
                            
def error(s):
    global loglevel
    if loglevel >= ERROR:
            __write(s,'ERROR')
