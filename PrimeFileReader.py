__author__ = 'john'

import struct
from PrimeFinder import PrimeFinder
from Log import Log

class PrimeFileReader(PrimeFinder):
    """
    Reads 4-byte unsigned integer binary primes in native byte order from the file given at construction time.
    This is as opposed to computing them, so it should go faster.  Note that `primesNotGreaterThan`
    may not return ALL primes not greater than the argument given to it, in the case that the file doesn't have
    enough primes.

    *Obsolete docstring:*

    Reads whitespace-separated primes from a text file.
    """

    def __init__(self, aFilePath):
        self._filePath = aFilePath

    def primesNotGreaterThan(self, aMaximum):
        retval = []
        # Binary file:
        with open( self._filePath, "rb") as f:
            b = f.read(4) # Four bytes
            while (b):
                p = struct.unpack( "I", b)[0];
                if (p <= aMaximum):
                    retval.append( p)
                    b = f.read(4)
                else:
                    break

        # Text file:
        # with open( aFilePath) as f:
        #     for line in f:
        #         primes = line.split()
        #         for p in primes:
        #             self._primes.append(p)

        # for p in self._primes:
        #     pint = int( p)
        #     if (pint <= aMaximum):
        #         retval.append( pint)
        #     else:
        #         break

        return retval

