#!/usr/bin/env python3

"""
validcall.py
Check for valid US callsign format

Version 1.0a

Steve de Bode - KQ4ZCI - December 2025

Input:  callsign
Output: exit code only:
 0      valid
 1      invalid
 2      scipt usage error
"""

import re
import sys

def is_valid_us_callsign(callsign: str) -> bool:
 callsign = callsign.strip().upper()

 # Remove optional portable suffixes
 callsign = re.sub(r"/(P|M|MM|AM)$", "", callsign)

 pattern = re.compile(
  r"^(?:"
  r"[KNW][A-Z]?|"    # K/N/W or KA–KZ, NA–NZ, WA–WZ
  r"A[A-L]"          # AA–AL
  r")"
  r"[0-9]"           # single digit
  r"[A-Z]{1,3}$"     # 1–3 letter suffix
 )

 return bool(pattern.match(callsign))


def main():
 if len(sys.argv) != 2:
  sys.exit(2)

 sys.exit(0 if is_valid_us_callsign(sys.argv[1]) else 1)


if __name__ == "__main__":
 main()
