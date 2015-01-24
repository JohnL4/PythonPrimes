import sys

__author__ = 'john'

def note( *objs):
    """
    Consider using the analogous method in `Log` instead of this global method, since the Log class might do something
    more intelligent (like log to a different file, or log to a database or log in XML or log asynchronously or whatever).
    """
    print( "NOTE:", *objs, file=sys.stderr)

def warn( *objs):
    print( "WARNING:", *objs, file=sys.stderr)

def error( *objs):
    print( "ERROR:", *objs, file=sys.stderr)

class Log:
    """
    Simple class to do logging.  Current implementation is just to send to output to stderr via global `note`, `warn`,
    `error` functions.
    """

    def note( *objs):
        note( *objs)

    def warn( *objs):
        warn( *objs)

    def error( *objs):
        error( *objs)