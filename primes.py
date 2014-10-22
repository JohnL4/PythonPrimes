#!/usr/bin/python3
import argparse

from datetime import datetime, timedelta
import sys
from Eratosthenes import Eratosthenes
from PrimeFinder import PrimeFinder

# primeCeiling = int(sys.argv[1])

argParser = argparse.ArgumentParser(description="Find prime numbers")
argParser.add_argument("--ceiling", type=int, help="Maximum prime number to be found")
argParser.add_argument("--count", type=int, help="Count of prime numbers to be found")
argParser.add_argument("--noprint", action="store_false", dest="print", default=True,
                       help="Don't actually print the found primes")
args = argParser.parse_args()

primeCeiling = args.ceiling
if (primeCeiling == None):
    primeCeiling = 100

# pf = PrimeFinder()
primeFinder = Eratosthenes()

startTime = datetime.now()
primes = primeFinder.primesNotGreaterThan(primeCeiling)
endTime = datetime.now()

if (args.print):
    for p in primes:
        print( "{0:7d} ".format( p),end="")
    print()

print("Found {0} primes in {1}".format(len(primes), (endTime - startTime)))
