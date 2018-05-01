#!/usr/bin/env python3

import sys

def __arg_parse(s):
    parts = s.split('=')
    if len(parts) == 2:
        return (parts[0], parts[1])
    else:
        sys.exit("could not parse '%s'" % s)

def args_parse(start=1):
    arg_dict = {}
    arg_list = sys.argv[start:]
    for arg in arg_list:
        (k,v) = __arg_parse(arg)
        arg_dict[k] = v
    return arg_dict

if __name__ == "__main__":
    arg_dict = args_parse()
    print(arg_dict)
