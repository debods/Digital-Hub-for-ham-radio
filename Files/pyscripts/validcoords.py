#!/usr/bin/env python3

"""
validcoords.py
Calculate APRS Password from ham callsign

Version 1.0a

Steve de Bode - KQ4ZCI - December 2025

Input:		Latitude Longitude
Exit codes: 0 = valid
			1 = invalid coordinates
			2 = invalid arguments
"""

import argparse
import sys

class SilentArgumentParser(argparse.ArgumentParser):
 def error(self, message):
  sys.exit(2)   # argparse-style error, but silent

def validate(latitude, longitude):
 if not (-90.0 <= latitude <= 90.0):
  return False

 if not (-180.0 <= longitude <= 180.0):
  return False

 return True

def main():
 parser = SilentArgumentParser(add_help=False)
 parser.add_argument("latitude", type=float)
 parser.add_argument("longitude", type=float)

 args = parser.parse_args()

 if not validate(args.latitude, args.longitude):
  sys.exit(1)

 sys.exit(0)

if __name__ == "__main__":
 main()