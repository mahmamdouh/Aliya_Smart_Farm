#Libraries
import RPi.GPIO as GPIO
from time import sleep
from Sys_Data import Alarm

def Buzzwr_Init():
    
    #Disable warnings (optional)
    GPIO.setwarnings(False)
    #Select GPIO mode
    GPIO.setmode(GPIO.BCM)
    #Set buzzer - pin # as output
    buzzer=7 
    GPIO.setup(buzzer,GPIO.OUT)
    
def Buzzer_Alarm_Runable():
    Buzzwr_Init()
    buzzer=7
    if Alarm["Staus"] == True:
        for i in range(20):
            GPIO.output(buzzer,GPIO.HIGH)
            sleep(0.5) # Delay in seconds
            GPIO.output(buzzer,GPIO.LOW)
            sleep(0.5)

