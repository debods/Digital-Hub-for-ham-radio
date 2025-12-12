#!/usr/bin/env python

#
# gpstest.py
# Find GPS device and connection
#
# Version 1.0a
#
# Steve de Bode - KQ4ZCI - December 2025
#

from serial.tools import list_ports
import serial

ser = None

for port in list_ports.comports():
 if "USB" in port.device or "ACM" or "tty" in port.device:
  try:
   ser = serial.Serial(port.device, 4800, timeout=10)
   print(f"{port.device}")
   break
  except serial.SerialException:
   pass

if ser is None:
 print("nogps")
