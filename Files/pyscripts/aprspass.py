#!/usr/bin/env python3

"""
hamgrid.py
Calculate APRS Password from ham callsign

Version 1.0a

Steve de Bode - KQ4ZCI - December 2025

Input:	callsign
Output: (APRS password)
"""

import re
import sys

PORTABLE_RE = re.compile(r"/(P|M|MM)$", re.IGNORECASE)

def normalize_callsign(callsign: str) -> str:
    cs = callsign.strip().upper()
    cs = PORTABLE_RE.sub("", cs)
    return cs

def aprs_passcode(callsign: str) -> int:
    # Normalize and strip portable/mobile suffixes
    cs = normalize_callsign(callsign)

    # APRS-IS passcode is based on the callsign only (SSID ignored)
    base = cs.split("-", 1)[0]

    h = 0x73E2
    for i, ch in enumerate(base):
        if i & 1:
            h ^= ord(ch)
        else:
            h ^= ord(ch) << 8

    return h & 0x7FFF

def main() -> int:
    if len(sys.argv) != 2:
        return 2

    cs = sys.argv[1]
    if not cs.strip():
        return 2

    print(aprs_passcode(cs))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
