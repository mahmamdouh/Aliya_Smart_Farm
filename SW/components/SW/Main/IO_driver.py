import RPi.GPIO as GPIO               # imports the GPIO lib
import time

# init Pin as output
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)               # disable warnings
GPIO.setup(17,GPIO.OUT)		  	          # LED connected to GPIO 2    wormer1
GPIO.setup(3,GPIO.OUT)		  	          # LED connected to GPIO 3    wormer2
GPIO.setup(2,GPIO.OUT)		  	          # LED connected to GPIO 5    wormer3

GPIO.setup(20,GPIO.OUT)		  	          # LED connected to GPIO 17   collar1
GPIO.setup(21,GPIO.OUT)		  	          # LED connected to GPIO 5    collar2
GPIO.setup(5,GPIO.OUT)		  	          # LED connected to GPIO 17   collar3



def Heater_1_OFF():
    GPIO.output(17, GPIO.LOW)
   # print("LED OFF")

def Heater_1_ON():
    GPIO.output(17, GPIO.HIGH)
    #print("LED ON")

def Heater_2_OFF():
    GPIO.output(3, GPIO.LOW)
   # print("LED OFF")

def Heater_2_ON():
    GPIO.output(3, GPIO.HIGH)
    #print("LED ON")

def Heater_3_OFF():
    GPIO.output(2, GPIO.LOW)
    #print("LED OFF")

def Heater_3_ON():
    GPIO.output(2, GPIO.HIGH)
    #print("LED ON")

def Collar_1_OFF():
    GPIO.output(20, GPIO.LOW)
    #print("LED OFF")


def Collar_1_ON():
    GPIO.output(20, GPIO.HIGH)
    #print("LED ON")


def Collar_2_OFF():
    GPIO.output(21, GPIO.LOW)
    #print("LED OFF")


def Collar_2_ON():
    GPIO.output(21, GPIO.HIGH)
    #print("LED ON")

def Collar_3_OFF():
    GPIO.output(5, GPIO.LOW)
    #print("LED OFF")


def Collar_3_ON():
    GPIO.output(5, GPIO.HIGH)
    #print("LED ON")