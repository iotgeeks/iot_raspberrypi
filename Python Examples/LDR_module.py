#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
 
cnl = 3
GPIO.setmode(GPIO.BOARD)
 
# PIN 7 AND 3.3V
# normally 0 when connected 1
GPIO.setup(cnl, GPIO.IN, GPIO.PUD_DOWN)
try:
    while(True):
        print(GPIO.input(cnl))
        print("LDR")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Exiting")
