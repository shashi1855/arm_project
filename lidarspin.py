#!/usr/bin/python
WaitTime = 0.001
import sys
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)  #motor1-step pin
GPIO.setup(16,GPIO.OUT)  #motor1-direction pin
GPIO.setup(22,GPIO.OUT)  #motor1-enable pin
GPIO.setup(8,GPIO.OUT)   #motor2-enable pin
GPIO.setup(10,GPIO.OUT)  #motor2-direction pin
GPIO.setup(12,GPIO.OUT)  #motor2-step pin

def Lidar_Spin():
    GPIO.output(22,False)
    GPIO.output(8, False)
    GPIO.output(16, True)
    GPIO.output(10, True)
    count = 0
    while(count < 801):
        GPIO.output(18, False)
        time.sleep(WaitTime)
        GPIO.output(18, True)
        time.sleep(WaitTime)
        count = count + 1
        print 'step:', count
for i in range(0,9):
    Lidar_Spin()
    print('motor1 completed one rotation')
    GPIO.output(12,False)
    time.sleep(WaitTime)
    GPIO.output(12,True)
    time.sleep(WaitTime)
    print('motor2 raised by one step')
    
