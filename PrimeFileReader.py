__author__ = 'john'

import struct
from PrimeFinder import PrimeFinder
from Log import Log

class PrimeFileReader(PrimeFinder):
    """
    Reads whitespace-separated primes from a text file, rather than computing them.  Note that `primesNotGreaterThan`
    may not return ALL primes not greater than the argument given to it.
    """

    def __init__(self, aFilePath):
        self._primes = []
        # Binary file:
        with open( aFilePath, "rb") as f:
            b = f.read(4) # Four bytes
            while (b):
                p = struct.unpack( "I", b)[0];
                self._primes.append( p)
                b = f.read(4)
        # Text file:
        # with open( aFilePath) as f:
        #     for line in f:
        #         primes = line.split()
        #         for p in primes:
        #             self._primes.append(p)

    def primesNotGreaterThan(self, aMaximum):
        retval = []
        for p in self._primes:
            pint = int( p)
            if (pint <= aMaximum):
                retval.append( pint)
            else:
                break
        return retval

