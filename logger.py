import datetime
import sys
import os
from traceback import extract_stack
from os.path import basename,splitext

TRACE = 5
INFO  = 4
SHOW  = 3
WARN  = 2
ERROR = 1
NONE  = 0
DEFAULT_LOGLEVEL = SHOW

def __write(s,l):
    if l == 'STACK':
        loc = str([(s[0],s[1],s[2]) for s in extract_stack()])
    elif l == 'TRACE':
        frame = extract_stack(limit=3)[0]
        loc = splitext(basename(frame[0]))[0] + '.' + frame[2] + '(' + str(frame[1]) + ')'
        loc = loc.ljust(30)
    else:
        frame = extract_stack(limit=3)[0][0]
        loc = splitext(basename(frame))[0].ljust(8)
    global logfile
    ts = datetime.datetime.now().strftime("%x %X")
    if s:
        logfile.write("%s %s [%s] -- %s\n" % (l, ts, loc, s))
    else:
        logfile.write("%s %s [%s]\n" % (l, ts, loc))
          
def stack_trace():
    global loglevel
    if loglevel >= TRACE:
        __write("",'STACK')

def trace(*args):
    global loglevel
    if loglevel >= TRACE:
        if args:
            __write(args[0],'TRACE')
        else:
            __write(None,'TRACE')
                            
def info(s):
    global loglevel
    if loglevel >= INFO:
        __write(s,'INFO ')
                            
def show(s):
    global loglevel
    if loglevel >= SHOW:
        __write(s,'SHOW ')
                            
def warn(s):
    global loglevel
    if loglevel >= WARN:
        __write(s,'WARN ')
                            
def error(s):
    global loglevel
    if loglevel >= ERROR:
        __write(s,'ERROR')

def set_loglevel(l):
    if isinstance(l,str):
        l = enumerate_loglevel(l)
    assert l in (NONE, ERROR, WARN, SHOW, INFO, TRACE)
    global loglevel
    loglevel = l


def enumerate_loglevel(s):
    _s = s.upper().strip()
    if 'NONE' == _s:
        return NONE
    elif 'ERROR'== _s:
        return ERROR
    elif 'WARN'== _s:
        return WARN
    elif 'SHOW'== _s:
        return SHOW
    elif 'INFO,'== _s:
        return INFO,
    elif 'TRACE'== _s:
        return TRACE
    else:
        return DEFAULT_LOGLEVEL



if sys.version_info < (3,6):
    sys.stderr.write("python version >= 3.6 is required")
    exit()

if 'loglevel' not in globals():
    logfile = sys.stderr
    env_loglevel = os.environ.get('loglevel')
    if env_loglevel:
        set_loglevel(env_loglevel)
        sys.stderr.write("setting loglevel from environment: [%s]\n" % env_loglevel)
    else:
        loglevel = DEFAULT_LOGLEVEL
