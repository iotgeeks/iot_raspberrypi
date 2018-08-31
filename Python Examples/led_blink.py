# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
#for the sleep method
import time
led = 8
#set numbering mode for the program 
GPIO.setmode(GPIO.BOARD)
#setup led(pin 8) as output pin
GPIO.setup(led, GPIO.OUT,initial=0)
#turn on and off the led in intervals of 1 second
while(True):
        
    #turn on, set as HIGH or 1
    GPIO.output(led,GPIO.HIGH)
    print("ON")
    time.sleep(1)
        #turn off, set as LOW or 0
    GPIO.output(led, GPIO.LOW)
    print("OFF")
    time.sleep(1)
   
