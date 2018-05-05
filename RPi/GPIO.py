# this is a fake RPIO libarary for tests on our mac's
# This does not need to go on Pi
# The whole RPi folder is part of this fakery.
# Pi already has the library installed

BOARD = 1
OUT = 1
IN = 1
BCM = 1
def setmode(a):
   print('in GPIO.setmode')
def setup(a, b):
   print('in GPIO.setup')
def output(a, b):
   print('in GPIO.output')
def cleanup():
   print('in GPIO.cleanup')
def setmode(a):
   print('in GPIO.setmode')
def setwarnings(flag):
   print('False')
