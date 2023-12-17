import RPi.GPIO as GPIO               # imports the GPIO lib
import time

# init Pin as output
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)               # disable warnings
GPIO.setup(0,GPIO.OUT)		  	          # LED connected to GPIO 0    wormer1
GPIO.setup(5,GPIO.OUT)		  	          # LED connected to GPIO 5    wormer2
GPIO.setup(6,GPIO.OUT)		  	          # LED connected to GPIO 6    wormer3

GPIO.setup(22,GPIO.OUT)		  	          # LED connected to GPIO 22   collar1
GPIO.setup(27,GPIO.OUT)		  	          # LED connected to GPIO 27    collar2
GPIO.setup(17,GPIO.OUT)		  	          # LED connected to GPIO 17   collar3



def Heater_1_OFF():
    GPIO.output(0, GPIO.LOW)
   # print("LED OFF")

def Heater_1_ON():
    GPIO.output(0, GPIO.HIGH)
    #print("LED ON")

def Heater_2_OFF():
    GPIO.output(5, GPIO.LOW)
   # print("LED OFF")

def Heater_2_ON():
    GPIO.output(5, GPIO.HIGH)
    #print("LED ON")

def Heater_3_OFF():
    GPIO.output(6, GPIO.LOW)
    #print("LED OFF")

def Heater_3_ON():
    GPIO.output(6, GPIO.HIGH)
    #print("LED ON")

def Collar_1_OFF():
    GPIO.output(22, GPIO.LOW)
    #print("LED OFF")


def Collar_1_ON():
    GPIO.output(22, GPIO.HIGH)
    #print("LED ON")


def Collar_2_OFF():
    GPIO.output(27, GPIO.LOW)
    #print("LED OFF")


def Collar_2_ON():
    GPIO.output(27, GPIO.HIGH)
    #print("LED ON")

def Collar_3_OFF():
    GPIO.output(17, GPIO.LOW)
    #print("LED OFF")


def Collar_3_ON():
    GPIO.output(17, GPIO.HIGH)
    #print("LED ON")