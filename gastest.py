import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN)
GPIO.setup(22,GPIO.IN)
GPIO.setup(10,GPIO.IN)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
time.sleep(1)
while(True):
    GPIO.output(6,GPIO.HIGH)
    GPIO.output(5,GPIO.HIGH)
    GPIO.output(11,GPIO.HIGH)
    GPIO.output(9,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(6,GPIO.LOW)
    GPIO.output(5,GPIO.LOW)
    GPIO.output(11,GPIO.LOW)
    GPIO.output(9,GPIO.LOW)
    if(GPIO.input(27) == GPIO.LOW) and (GPIO.input(22) == GPIO.LOW) and (GPIO.input(10) == GPIO.LOW):
        gas = 20
    if(GPIO.input(27) == GPIO.LOW) and (GPIO.input(22) == GPIO.LOW) and (GPIO.input(10) == GPIO.HIGH):
        gas = 30
    if(GPIO.input(27) == GPIO.LOW) and (GPIO.input(22) == GPIO.HIGH) and (GPIO.input(10) == GPIO.LOW):
        gas = 40
    if(GPIO.input(27) == GPIO.LOW) and (GPIO.input(22) == GPIO.HIGH) and (GPIO.input(10) == GPIO.HIGH):
        gas = 50
    if(GPIO.input(27) == GPIO.HIGH) and (GPIO.input(22) == GPIO.LOW) and (GPIO.input(10) == GPIO.LOW):
        gas = 60
    if(GPIO.input(27) == GPIO.HIGH) and (GPIO.input(22) == GPIO.LOW) and (GPIO.input(10) == GPIO.HIGH):
        gas = 70
    if(GPIO.input(27) == GPIO.HIGH) and (GPIO.input(22) == GPIO.HIGH) and (GPIO.input(10) == GPIO.LOW):
        gas = 80
    if(GPIO.input(27) == GPIO.HIGH) and (GPIO.input(22) == GPIO.HIGH) and (GPIO.input(10) == GPIO.HIGH):
        gas = 90
    print gas
    time.sleep(2)
    
    
