import RPi.GPIO as GPIO
import time
import random
from sensor import distance

GPIO.setwarnings(False)
front_echo = 1
front_trigger = 7
rear_echo = 17
rear_trigger = 27

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.OUT) # right side motor
    GPIO.setup(13, GPIO.OUT) # right side motor
    GPIO.setup(19, GPIO.OUT) # left side motor
    GPIO.setup(26, GPIO.OUT) # left side motor
    
    # front sensor setup
    GPIO.setup(front_echo, GPIO.IN)
    GPIO.setup(front_trigger, GPIO.OUT)
    # rear sensor setup
    GPIO.setup(rear_echo, GPIO.IN)
    GPIO.setup(rear_trigger, GPIO.OUT)


def forward(time_frame):
    print('GOING FORWARD')
    init()
    GPIO.output(6, False) # right side wheels / input 1 & 2
    GPIO.output(13, True) # right side wheels input 1 & 2
    GPIO.output(19, False) # left side wheels / input 3 & 4
    GPIO.output(26, True) # left side wheels / input 3 & 4
    time.sleep(time_frame)
    GPIO.cleanup()

def pivot_left(time_frame):
    print('Pivoting left')
    init()
    GPIO.output(6, False)
    GPIO.output(13, True)
    GPIO.output(19, True)
    GPIO.output(26, False)
    time.sleep(time_frame)
    GPIO.cleanup()

def pivot_right(time_frame):
    print('Pivoting right')
    init()
    GPIO.output(6, True)
    GPIO.output(13, False)
    GPIO.output(19, False)
    GPIO.output(26, True)
    time.sleep(time_frame)
    GPIO.cleanup()

def reverse(time_frame):
    print('REVERSING')
    init()
    GPIO.output(6, True) # right side wheels / input 1 & 2
    GPIO.output(13, False) # right side wheels input 1 & 2
    GPIO.output(19, True) # left side wheels / input 3 & 4
    GPIO.output(26, False) # left side wheels / input 3 & 4
    time.sleep(time_frame)
    GPIO.cleanup()

def turn_right(time_frame):
    print('turning right')
    init()
    GPIO.output(6, False)
    GPIO.output(13, False)
    GPIO.output(19, False)
    GPIO.output(26, True)
    time.sleep(time_frame)
    GPIO.cleanup()

def turn_left(time_frame):
    print('turning left')
    init()
    GPIO.output(6, False)
    GPIO.output(13, True)
    GPIO.output(19, False)
    GPIO.output(26, False)
    time.sleep(time_frame)
    GPIO.cleanup()

init()

####### move forward until hazzard found, then reverse and turn right
# while(distance(front_echo, front_trigger) > 25 ):
#    forward(0.5)

while (distance(front_echo, front_trigger) > 25):
    forward(0.2)

#reverse(2)
#turn_right(3)

pivot_right(3)
pivot_left(3)
