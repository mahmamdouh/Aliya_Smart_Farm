##################################################################
##																##
##		   /\		|		|	\		/		/\				##
##		  /	 \		|		|    \     /	   /  \			    ##
##		 /	  \		|		|	  \   /		  /	   \		    ##
##		/------\	|		|	   \ /	   	 /------\			##
##	   /	 	\	|_____	|	|___/		/		 \			##
## 																##
## 			    	Aliya Smart System							##
## 			         WWW.Aliya-Co.com							##
##################################################################
##################################################################
##  Project        : Aliya-Smart-Farm                           ##
##	component name : Read Correct Filter						##
##	Author         : Mahmoud Elmohtady							##
##	Date           : 31/10/2021									##
##																##
##																##
##################################################################

##################################################################
####                  Liberary Include                        ####
##################################################################
import RPi.GPIO as GPIO
import dht11
import time
import datetime
from datetime import date
## to be removed
from openpyxl import load_workbook
import numpy  # Import numpy
import pandas as pd
from DTC import DHT_DIAG_Update
from Correct_Filter import Correct_factor_runable
from Sys_Data import DHT_Temp_Reading

##################################################################
####               Define Global variable                     ####
##################################################################

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
sensor1 = dht11.DHT11(pin=16)
sensor2 = dht11.DHT11(pin=20)
sensor3 = dht11.DHT11(pin=21)
sensor4 = dht11.DHT11(pin=7)
sensor5 = dht11.DHT11(pin=12)
sensor6 = dht11.DHT11(pin=23)

# ErrorFactor
Temp_Error_Factor = 2
Humid_Error_Factor = 10




##################################################################
####                Function Definition                       ####
##################################################################


#######################################################################
# function name :                                                     #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
def DHT_Update_10_min():
    DHT_Temp_Reading,DHT_Humid_Reading=DHT_Get_Readings()

    # check How many number of readings Back
    if DHT_Temp_Reading["Readings"] == 0 :
        # return Zero value
        return 0,0
    elif DHT_Temp_Reading["Readings"] == 1 :
        #return only one value
        return (sum(DHT_Temp_Reading.values())),(sum(DHT_Humid_Reading.values()))
    elif DHT_Temp_Reading["Readings"] > 1 :
        # Get correct values
        DHT_Temp_Reading = Correct_factor_runable(DHT_Temp_Reading,Temp_Error_Factor)
        DHT_Humid_Reading = Correct_factor_runable(DHT_Humid_Reading,Humid_Error_Factor)

        # calculate number of correct readings return back
        nubmer_of_Teamp_reading_correct = len(DHT_Temp_Reading.keys())
        nubmer_of_humid_reading_correct = len(DHT_Humid_Reading.keys())

        #Sum of total readings
        Temp_total = sum(DHT_Temp_Reading.values())
        Humid_total = sum(DHT_Humid_Reading.values())

        # Average of readings
        DHT_OverAll_Temp  = Temp_total/nubmer_of_Teamp_reading_correct
        DHT_OverAll_humid = Humid_total/nubmer_of_humid_reading_correct
        return (DHT_OverAll_Temp ,DHT_OverAll_humid)
    else:
        return 0,0

       

#######################################################################
# function name :  DHT_Get_sensor_Read                                #
# Inputs :  sensor number                                             #
# Outputs :  sensor reading ( teamp - humid )                         #
# Description :  get sensor read                                      #
# Function Scope : ( Local)                                           #
# Arch ID :                                                           #
#######################################################################

def DHT_Get_sensor_Read(Sensor):
    if Sensor == 1:
        try:
            result1 = sensor1.read()
            time.sleep(2)
        except:
            DHT_DIAG_Update("DTC_1");
        if result1.is_valid():
            print("getting sensor 1 readings")
            print("Last valid input from sensor 1: " + str(datetime.datetime.now()))
            print("Temperature: %-3.1f C" % result1.temperature)
            print("Humidity: %-3.1f %%" % result1.humidity)
            return (result1.temperature,result1.humidity)
        else:
            DHT_DIAG_Update("DTC_1");
            return 0
    elif Sensor == 2:
        try:
            result2 = sensor2.read()
            time.sleep(2)
        except:
            DHT_DIAG_Update("DTC_2");
        if result2.is_valid():
            print("getting sensor 2 readings")
            print("Last valid input from sensor 2: " + str(datetime.datetime.now()))
            print("Temperature: %-3.1f C" % result2.temperature)
            print("Humidity: %-3.1f %%" % result2.humidity)
            return result2.temperature ,result2.humidity
        else:
            DHT_DIAG_Update("DTC_2");
            return 0
    elif Sensor == 3:
        try:
            result3 = sensor3.read()
            time.sleep(2)
        except:
            DHT_DIAG_Update("DTC_3");
        if result3.is_valid():
            print("getting sensor 3 readings")
            print("Last valid input from sensor 3: " + str(datetime.datetime.now()))
            print("Temperature: %-3.1f C" % result3.temperature)
            print("Humidity: %-3.1f %%" % result3.humidity)
            return result3.temperature ,result3.humidity
        else:
            DHT_DIAG_Update("DTC_3");
            return 0
    elif Sensor == 4:
        try:
            result4 = sensor4.read()
            time.sleep(2)
        except:
            DHT_DIAG_Update("DTC_4");
        if result4.is_valid():
            print("getting sensor 4 readings")
            print("Last valid input from sensor 4: " + str(datetime.datetime.now()))
            print("Temperature: %-3.1f C" % result4.temperature)
            print("Humidity: %-3.1f %%" % result4.humidity)
            return result4.temperature ,result4.humidity
        else:
            DHT_DIAG_Update("DTC_4");
            return 0
    elif Sensor == 5:
        try:
            result5 = sensor5.read()
            time.sleep(2)
        except:
            DHT_DIAG_Update("DTC_5");
        if result5.is_valid():
            print("getting sensor 5 readings")
            print("Last valid input from sensor 5: " + str(datetime.datetime.now()))
            print("Temperature: %-3.1f C" % result5.temperature)
            print("Humidity: %-3.1f %%" % result5.humidity)
            return result5.temperature ,result5.humidity
        else:
            DHT_DIAG_Update("DTC_5");
            return 0
    elif Sensor == 6:
        try:
            result6 = sensor6.read()
            time.sleep(2)
        except:
            DHT_DIAG_Update("DTC_6");
        if result6.is_valid():
            print("getting sensor 6 readings")
            print("Last valid input from sensor 6: " + str(datetime.datetime.now()))
            print("Temperature: %-3.1f C" % result6.temperature)
            print("Humidity: %-3.1f %%" % result6.humidity)
            return result6.temperature ,result6.humidity
        else:
            DHT_DIAG_Update("DTC_6");
            return 0
    else:
        return 0



#######################################################################
# function name :                                                     #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
def Check_sensor_Read_failure(Sensor_reading):
        if "Sensor 1" in Sensor_reading:
            print("Sensor 1 exists") 
        else:
            DHT_DIAG_Update("DTC_7")
        if "Sensor 2" in Sensor_reading:
            print("Sensor 2 exists") 
        else:
            DHT_DIAG_Update("DTC_8")
        if "Sensor 3" in Sensor_reading:
            print("Sensor 3 exists") 
        else:
            DHT_DIAG_Update("DTC_9")
        if "Sensor 4" in Sensor_reading:
            print("Sensor 4 exists") 
        else:
            DHT_DIAG_Update("DTC_10")
        if "Sensor 5" in Sensor_reading:
            print("Sensor 5 exists") 
        else:
            DHT_DIAG_Update("DTC_11")
        if "Sensor 6" in Sensor_reading:
            print("Sensor 6 exists") 
        else:
            DHT_DIAG_Update("DTC_12")


#######################################################################
# function name : DHT_Get_Readings                                    #
# Inputs :  non                                                       #
# Outputs :       dictionary of reading, number of readings           #
# Description :                                                       #
# Function Scope : ( Local  )                                         #
# Arch ID :                                                           #
#######################################################################

def DHT_Get_Readings():
    Tamprature=0
    Humidety=0
    DHT_Temp_Reading = {
        "Readings": 0,
    }
    DHT_Humid_Reading = {
        "Readings": 0,
    }
    # Get sensor 1 reading
    for i in range(4):
        Tamprature ,Humidety =DHT_Get_sensor_Read(1)
        if Tamprature != 0:
            DHT_Temp_Reading["Sensor 1"]=Tamprature
            DHT_Humid_Reading["Sensor 1"]=Humidety
            DHT_Temp_Reading["Readings"]=DHT_Temp_Reading["Readings"]+1
            break
    # Log DTC of read = 0
    if Tamprature == 0:
        DHT_DIAG_Update("DTC_7")

    # Get sensor 2 reading
    for i in range(4):
        Tamprature ,Humidety =DHT_Get_sensor_Read(2)
        if Tamprature != 0:
            DHT_Temp_Reading["Sensor 2"]=Tamprature
            DHT_Humid_Reading["Sensor 2"]=Humidety
            DHT_Temp_Reading["Readings"] = DHT_Temp_Reading["Readings"] + 1
            break
    # Log DTC of read = 0
    if Tamprature == 0:
        DHT_DIAG_Update("DTC_8")

    # Get sensor 3 reading
    for i in range(4):
        Tamprature ,Humidety =DHT_Get_sensor_Read(3)
        if Tamprature != 0:
            DHT_Temp_Reading["Sensor 3"]=Tamprature
            DHT_Humid_Reading["Sensor 3"]=Humidety
            DHT_Temp_Reading["Readings"] = DHT_Temp_Reading["Readings"] + 1
            break
    # Log DTC of read = 0
    if Tamprature == 0:
        DHT_DIAG_Update("DTC_9")

    # Get sensor4  reading
    for i in range(4):
        Tamprature ,Humidety =DHT_Get_sensor_Read(4)
        if Tamprature != 0:
            DHT_Temp_Reading["Sensor 4"]=Tamprature
            DHT_Humid_Reading["Sensor 4"]=Humidety
            DHT_Temp_Reading["Readings"] = DHT_Temp_Reading["Readings"] + 1
            break
    # Log DTC of read = 0
    if Tamprature == 0:
        DHT_DIAG_Update("DTC_10")

    # Get sensor 5 reading
    for i in range(4):
        Tamprature ,Humidety =DHT_Get_sensor_Read(5)
        if Tamprature != 0:
            DHT_Temp_Reading["Sensor 5"]=Tamprature
            DHT_Humid_Reading["Sensor 5"]=Humidety
            DHT_Temp_Reading["Readings"] = DHT_Temp_Reading["Readings"] + 1
            break
    # Log DTC of read = 0
    if Tamprature == 0:
        DHT_DIAG_Update("DTC_11")

    # Get sensor 6 reading
    for i in range(4):
        Tamprature ,Humidety =DHT_Get_sensor_Read(6)
        if Tamprature != 0:
            DHT_Temp_Reading["Sensor 6"]=Tamprature
            DHT_Humid_Reading["Sensor 6"]=Humidety
            DHT_Temp_Reading["Readings"] = DHT_Temp_Reading["Readings"] + 1
            break
    # Log DTC of read = 0
    if Tamprature == 0:
        DHT_DIAG_Update("DTC_12")

    return DHT_Temp_Reading ,DHT_Humid_Reading