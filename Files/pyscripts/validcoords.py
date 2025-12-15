#!/usr/bin/env python3

"""
validcoords.py
Calculate APRS Password from ham callsign

Version 1.0a

Steve de Bode - KQ4ZCI - December 2025

Input:	Latitude Longitude
Output: validation
"""

import argparse
import sys

def validate(latitude, longitude):
    if latitude < -90.0 or latitude > 90.0:
        raise ValueError("Latitude must be between -90 and 90 degrees")

    if longitude < -180.0 or longitude > 180.0:
        raise ValueError("Longitude must be between -180 and 180 degrees")

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Validate latitude and longitude"
    )
    parser.add_argument("latitude", type=float)
    parser.add_argument("longitude", type=float)
    args = parser.parse_args()

    try:
        validate(args.latitude, args.longitude)
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
