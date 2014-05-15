#!/usr/bin/env python

import sys, os, getopt

def usage():
    print """
    Usage: commandline.py [options ...]
    -e : Exchange name
    -c : user -defined category name
    -f : read stock info from file and save to do"
    -d : delete from db by stock code
    -n : stock name
    -s : stock code
    -h : "this help info"
    """

try:
    opts, args = getopt.getopt(sys.argv[1:], 'he:c:f:d:n:s:')
except getopt.GetoptError:
    usage()
    sys.exit()
if len(opts) == 0:
    usage()
    sys.exit()

for opt, arg in opts:
    if opt in ('-h', '--help'):
        usage()
        sys.exit()
    elif opt == '-d':
        print "del stock %s" % arg
    elif opt == '-f':
        print 'read file %s' % arg

            
