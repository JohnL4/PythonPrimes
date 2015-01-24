__author__ = 'john'

class PrimeFinder:
    """Abstract base class for classes that find prime numbers."""

    def primesNotGreaterThan(self, aMaximum):
        """Returns a list of primes all of which are less than aMaximum."""
        # This implementation is stupid on purpose.
        somePrimes = [2,3,5,7]
        retval = []
        i = 0
        while (i < len(somePrimes)):
            if (somePrimes[i] <= aMaximum):
                retval.append( somePrimes[i])
            else:
                break
            i += 1
        return retval
