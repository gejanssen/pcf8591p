#!/usr/bin/python
#https://www.raspberrypi.org/forums/viewtopic.php?f=42&t=14093

import smbus
import time

bus = smbus.SMBus(1)

aout = 0

while True:

   for a in range(0,4):
      bus.write_byte_data(0x48,0x40 | ((a+1) & 0x03), 0)
      v = bus.read_byte(0x48)
      print v,
      time.sleep(0.1)

   print
