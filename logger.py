import datetime
import sys

TRACE = 4
INFO  = 3
WARN  = 2
ERROR = 1
NONE  = 0

loglevel = NONE 
logfile = sys.stderr

def __write(s,l):
    global logfile
    ts = datetime.datetime.now().strftime("%x %X")
    logfile.write("%s [%s] %s -- %s" % (ts, self.name.ljust(8),l, s))
          
def trace(s):
    global loglevel
    if loglevel >= TRACE or self.loglevel >= TRACE:
            __write(s,'TRACE')
                            
def info(s):
    global loglevel
    if loglevel >= INFO or self.loglevel >= INFO:
            __write(s,'INFO ')
                            
def warn(s):
    global loglevel
    if loglevel >= WARN or self.loglevel >= WARN:
            __write(s,'WARN ')
                            
def error(s):
    global loglevel
    if loglevel >= ERROR or self.loglevel >= ERROR:
            __write(s,'ERROR')
