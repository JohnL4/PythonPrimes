from math import sqrt, trunc
from PrimeFinder import PrimeFinder

__author__ = 'john'

class Sundaram(PrimeFinder):
    """
    Finds primes using Sundaram's sieve

    Note: Currently, this is significantly slower than Eratosthenes.  I'm sure I've done something wrong, but I
    don't immediately know what.  There is some discussion of Sundaram vs. Eratosthenes on the net, but I'm not
    in the mood right now to understand it.
    """

    def primesNotGreaterThan(self, aMaximum):

        # We'll be spitting out primes of the form 2n+1 <= aMaximum,
        # so we need n <= (aMaximum - 1) / 2

        n = int( trunc (aMaximum - 1) / 2)

        isPrime = [True for i in range(n+1)]

        # Remove all i + j + 2ij <= n
        #     i + j * (1 + 2i) <= n
        #     j <= (n - i) / (1 + 2 * i)

        maxJ = maxI = trunc((n - 1) / (1 + 2))
        for i in range(1, maxI+1):
            for j in range(1, maxJ+1):
                k = i + j + 2 * i * j
                if (k <= n):
                    isPrime[k] = False
                else:
                    break # Inner loop

        retval = [2]
        for i in range(1,n+1):
            if (isPrime[i]):
                retval.append( 2 * i + 1)

        return retval
