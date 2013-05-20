#!/usr/local/bin/idle -r
url = "http://www.python.org/ftp/python/2.7.1/python-2.7.1-macosx10.3.dmg"

import sys
assert sys.version.startswith('2.7.'), \
       "You need Python 2.7. Please download and install it from:\n" \
       "  " + url
assert sys.maxint == (2 ** 31 - 1), \
       "You need a 32-bit version of Python on Mac OS X. Please contact sfllaw@sfllaw.ca for help!"
try:
    import Tkinter
except ImportError:
    raise AssertionError("You need to install Python 2.7 from the Python website:\n"
                         "  " + url)
print "You installed Python 2.7 successfully!"
