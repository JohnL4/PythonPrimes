from math import sqrt, trunc
from PrimeFinder import PrimeFinder

__author__ = 'john'

class Eratosthenes(PrimeFinder):
    """Finds primes using the Sieve of Eratosthenes."""

    def primesNotGreaterThan(self, aMaximum):

        isPrime = [True for i in range(aMaximum+1)]
        isPrime[0] = isPrime[1] = False

        rootMax = trunc( sqrt(aMaximum+1))

        for i in range(2, rootMax+1):
            if isPrime[i]:
                for j in range( 2*i,aMaximum+1,i):
                    isPrime[j] = False

        retval = []
        for i in range(aMaximum+1):
            if isPrime[i]:
                retval.append(i)

        return retval