#!/usr/bin/python3
import argparse
import struct
import re
from datetime import datetime

from Log import Log
from Eratosthenes import Eratosthenes
from PrimeFileReader import PrimeFileReader
from Sundaram import Sundaram

# primeCeiling = int(sys.argv[1])

argParser = argparse.ArgumentParser(description="Find prime numbers")
argParser.add_argument( "--algorithm", type=str,
                        help="Algorithm to use; either Eratosthenes or Sundaram (can be abbreviated with a unique prefix")
argParser.add_argument("--ceiling", type=int, help="Maximum prime number to be found")
argParser.add_argument("--count", type=int, help="Count of prime numbers to be found")
argParser.add_argument("--noprint", action="store_false", dest="print", default=True,
                       help="Don't actually print the found primes")
argParser.add_argument( "--fromFile", type=str,
                        help="Name of a file from which to take primes (stored as binary), all of which are assumed to be prime already")
argParser.add_argument( "--toFile", type=str,
                        help="Name of a file into which to write primes, as binary")
args = argParser.parse_args()

algorithm = args.algorithm
if (algorithm == None):
    algorithm = "Eratosthenes"

if (re.match( algorithm + ".*", "Eratosthenes", re.IGNORECASE)):
    algorithm = "Eratosthenes"
elif (re.match( algorithm + ".*", "Sundaram", re.IGNORECASE)):
    algorithm = "Sundaram"
else:
    Log.error( "Supplied algorithm (\"{0}\") must be one of Eratosthenes or Sundaram; assuming Eratosthenes".format( algorithm))
    algorithm = "Eratosthenes"

primeCeiling = args.ceiling
if (primeCeiling == None):
    primeCeiling = 100

# pf = PrimeFinder()
fromFile = args.fromFile
toFile = args.toFile

if (fromFile):
    primeFinder = PrimeFileReader( fromFile)
elif (algorithm == "Eratosthenes"):
    primeFinder = Eratosthenes()
elif (algorithm == "Sundaram"):
    primeFinder = Sundaram()
else:
    Log.error( "Unexpected algorithm: {0}".format( algorithm))
    exit(1)

startTime = datetime.now()
primes = primeFinder.primesNotGreaterThan(primeCeiling)
endTime = datetime.now()

if (args.print):
    if (toFile):
        with open( toFile, "wb") as binFile:
            for p in primes:
                binFile.write( struct.pack( "I", p))
    else:
        for p in primes:
            print( "{0:7d} ".format( p),end="")
        print()

Log.note("Found {0} primes in {1}".format(len(primes), (endTime - startTime)))
