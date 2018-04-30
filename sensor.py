import RPi.GPIO as GPIO
import time

def init(echo, trigger):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(echo, GPIO.IN) #Echo pin
    GPIO.setup(trigger, GPIO.OUT) # Trigger pin

def distance(echo, trigger, measure_unit = 'cm'):
    init(echo, trigger)
    GPIO.output(trigger, False)
    # this is the bit your code was missing sending the trigger pulse
    print("Ultrasonic measurement")

    # Allow module to settle
    #time.sleep(0.01)

    # Send echo0us pulse to trigger
    GPIO.output(trigger, True)
    time.sleep(0.00001)
    GPIO.output(trigger, False)
    no_signal = time.time()
    signal = time.time()
    while GPIO.input(echo) == 0:
        print('in first echo')
        no_signal = time.time()


    while GPIO.input(echo) == echo:
        print('in second echo')
        signal = time.time()

    tl = signal - no_signal

    if measure_unit == "cm":
        distance = tl / 0.000058
    elif measure_unit == "in":
        distance = tl / 0.000148
    else:
        print('improper choice of measurement: in or cm')
        distance = None

    print(distance)
    return distance
