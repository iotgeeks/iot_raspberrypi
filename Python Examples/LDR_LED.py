#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
led=8
ldr = 3
GPIO.setmode(GPIO.BOARD)
 
# PIN 7 AND 3.3V
# normally 0 when connected 1
GPIO.setup(ldr, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(led, GPIO.OUT,initial=0)
try:
    while(True):
        print(GPIO.input(ldr))
        if(GPIO.input(ldr)):
            GPIO.output(led,GPIO.HIGH)
            print("ON")
        else:
            GPIO.output(led,GPIO.LOW)
            print("OFF")

        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Exiting")
