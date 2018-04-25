import datetime
import sys
from traceback import extract_stack
from os.path import basename,splitext

TRACE = 4
INFO  = 3
WARN  = 2
ERROR = 1
NONE  = 0

loglevel = TRACE
logfile = sys.stderr

def __write(s,l):
    if l == 'TRACE':
        #print(extract_stack())
        frame = extract_stack(limit=3)[0]
        loc = splitext(basename(frame[0]))[0] + '.' + frame[2] + '(' + str(frame[1]) + ')'
        loc = loc.ljust(30)
    else:
        frame = extract_stack(limit=3)[0][0]
        loc = splitext(basename(frame))[0].ljust(8)
    global logfile
    ts = datetime.datetime.now().strftime("%x %X")
    logfile.write("%s %s [%s] -- %s\n" % (l, ts, loc, s))
          
def debug(s):
    global loglevel
    if loglevel >= DEBUG:
            __write(s,'DEBUG')
                            
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
