'Car Module'
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
FRONT_ECHO = 1
FRONT_TRIGGER = 7
REAR_ECHO = 17
REAR_TRIGGER = 27

def init():
    'Init'
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.OUT) # right side motor
    GPIO.setup(13, GPIO.OUT) # right side motor
    GPIO.setup(19, GPIO.OUT) # left side motor
    GPIO.setup(26, GPIO.OUT) # left side motor

    # front sensor setup
    GPIO.setup(FRONT_ECHO, GPIO.IN)
    GPIO.setup(FRONT_TRIGGER, GPIO.OUT)
    # rear sensor setup
    GPIO.setup(REAR_ECHO, GPIO.IN)
    GPIO.setup(REAR_TRIGGER, GPIO.OUT)

def forward(time_frame):
    'Forward'
    print('GOING FORWARD')
    init()
    GPIO.output(6, False) # right side wheels / input 1 & 2
    GPIO.output(13, True) # right side wheels input 1 & 2
    GPIO.output(19, False) # left side wheels / input 3 & 4
    GPIO.output(26, True) # left side wheels / input 3 & 4
    time.sleep(time_frame)
    GPIO.cleanup()
    return True

def pivot_left(time_frame):
    'Left'
    print('PIVOTING LEFT')
    init()
    GPIO.output(6, False)
    GPIO.output(13, True)
    GPIO.output(19, True)
    GPIO.output(26, False)
    time.sleep(time_frame)
    GPIO.cleanup()
    return True

def pivot_right(time_frame):
    'Right'
    print('PIVOTING RIGHT')
    init()
    GPIO.output(6, True)
    GPIO.output(13, False)
    GPIO.output(19, False)
    GPIO.output(26, True)
    time.sleep(time_frame)
    GPIO.cleanup()
    return True

def reverse(time_frame):
    'Reverse'
    print('REVERSING')
    init()
    GPIO.output(6, True) # right side wheels / input 1 & 2
    GPIO.output(13, False) # right side wheels input 1 & 2
    GPIO.output(19, True) # left side wheels / input 3 & 4
    GPIO.output(26, False) # left side wheels / input 3 & 4
    time.sleep(time_frame)
    GPIO.cleanup()
    return True

def turn_right(time_frame):
    'Right'
    print('turning right')
    init()
    GPIO.output(6, False)
    GPIO.output(13, False)
    GPIO.output(19, False)
    GPIO.output(26, True)
    time.sleep(time_frame)
    GPIO.cleanup()
    return True

def turn_left(time_frame):
    'Left'
    print('turning left')
    init()
    GPIO.output(6, False)
    GPIO.output(13, True)
    GPIO.output(19, False)
    GPIO.output(26, False)
    time.sleep(time_frame)
    GPIO.cleanup()
    return True
