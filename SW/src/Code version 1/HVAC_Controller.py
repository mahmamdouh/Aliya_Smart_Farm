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
##	component name : HVAC_Controller						##
##	Author         : Mahmoud Elmohtady							##
##	Date           : 31/10/2021									##
##																##
##																##
##################################################################

##################################################################
####                  Liberary Include                        ####
##################################################################

import sys
import time
import datetime
from datetime import datetime
from Time_Control import Timer_Start,Five_Minuts,Timer_Cancel,Timer_Check
#from  IO_driver import Heater_1_OFF ,Heater_1_ON ,Heater_2_OFF ,Heater_2_ON ,Heater_3_OFF ,Heater_3_ON ,Collar_1_OFF ,Collar_1_ON ,Collar_2_OFF ,Collar_2_ON ,Collar_3_OFF ,Collar_3_ON
from Sys_Data import HVAC_sys_sts,Limits,HVAC_Active_Time,HVAC_STM
import threading
##################################################################
####               Define Global variable                     ####
##################################################################


# Hmid limits
Humid_Lw_limit = 10
Humid_Up_limit = 40

Wait_STM = {
  "Flag": False,
  "Flag_Running": False,
}

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
# update limits of temp
def Hvac_Set_Limits(TL,TU,HL,HU):
    # Temp limits
    Limits["Temp_Lw_limit"] = TL
    Limits["Temp_Up_limit"] = TU

    # Hmid limits
    Limits["Humid_Lw_limit"]= HL
    Limits["Humid_Up_limit"] = HU


#######################################################################
# function name :                                                     #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
#Get temp limits
def Hvac_Get_Limits():
    return Limits["Temp_Lw_limit"] ,Limits["Temp_Up_limit"] 

#######################################################################
# function name :                                                     #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
#Get temp limits

# States
#1- SB
#2- Coling
#3- Coling_wait
#2- Warming
#3- Warming_wait
def Hvac_Control_Runnable(Temp):
    # State machine Control
    
    HVAC_STM_Run(Temp)
    if HVAC_STM["State"] == "SB":
        HVAC_SB()
    elif HVAC_STM["State"] == "Coling":
        HVAC_Coling()
    elif HVAC_STM["State"] == "Coling_wait":
        HVAC_Coling_wait(Temp)
    elif HVAC_STM["State"] == "Warming":
        HVAC_Warming()
    elif HVAC_STM["State"] == "Warming_wait":
        HVAC_Warming_wait(Temp)

def HVAC_STM_Run(Temp):
    # State machine Control
    ## check SB mode
    #print("temp =====================================",Temp)
    #print("start of STM ",HVAC_STM , Limits)
    if HVAC_STM["State"] == "SB":
        if(Temp < Limits["Temp_Lw_limit"]):
            HVAC_STM["State"] = "Warming_wait"
            HVAC_STM["Previous_state"]= "SB"
        elif(Temp >  Limits["Temp_Up_limit"]):
            HVAC_STM["State"] = "Coling_wait"
            HVAC_STM["Previous_state"]= "SB"
        else:
            print("back to SB")
            HVAC_STM["State"] = "SB"
            HVAC_STM["Previous_state"]= "SB"

    ## check Warming mode    
    elif HVAC_STM["State"] == "Warming":
        if(Temp > Limits["Temp_Lw_limit"]):
            HVAC_STM["State"] = "Warming_wait"
            HVAC_STM["Previous_state"]= "Warming"
        elif(Temp < Limits["Temp_Lw_limit"]):
            HVAC_STM["State"] = "Warming"
            HVAC_STM["Previous_state"]= "Warming_wait"
    ## check Coling mode
    elif HVAC_STM["State"] == "Coling":
        if(Temp <  Limits["Temp_Up_limit"]):
            HVAC_STM["State"] = "Coling_wait"
            HVAC_STM["Previous_state"]= "Coling"
        elif(Temp >  Limits["Temp_Up_limit"]):
            HVAC_STM["State"] = "Coling"
            HVAC_STM["Previous_state"]= "Coling_wait"
    ## check Coling)wait mode
    elif HVAC_STM["State"] == "Coling_wait":
        HVAC_Coling_wait(Temp)
    ## check Warming_wait mode
    elif HVAC_STM["State"] == "Warming_wait":
        HVAC_Warming_wait(Temp)
    #print("temp and =====================================",Temp)
    #print("start of STM ",HVAC_STM)
    
def HVAC_Warming():
    HVAC_STM["State"] = "Warming"
    Heater_1_ON()
    Heater_2_ON()
    Heater_3_ON()
    Collar_1_OFF()
    Collar_2_OFF()
    Collar_3_OFF()



def HVAC_Coling():
    HVAC_STM["State"] = "Coling"
    Heater_1_OFF()
    Heater_2_OFF()
    Heater_3_OFF()
    Collar_1_ON()
    Collar_2_ON()
    Collar_3_ON()
    
def HVAC_SB():
    Heater_1_OFF()
    Heater_2_OFF()
    Heater_3_OFF()
    Collar_1_OFF()
    Collar_2_OFF()
    Collar_3_OFF()
    
def HVAC_Coling_wait(Temp):
    Timer_Check(5)
    if Five_Minuts["Flag"] == False :
        Timer_Start()
    if Five_Minuts["Flag"] == True :
        Timer_Cancel()
        print("CHeck colling wait",Temp,Limits)
        if(Temp >  Limits["Temp_Up_limit"]):
              HVAC_STM["State"] = "Coling"
        elif(Temp <  Limits["Temp_Up_limit"]):
             HVAC_STM["State"] = "SB"
    HVAC_SB()
def HVAC_Warming_wait(Temp):
    Timer_Check(5)
    if Five_Minuts["Flag"] == False :
        Timer_Start()
    if Five_Minuts["Flag"] == True :
        Timer_Cancel()
        if(Temp < Limits["Temp_Lw_limit"]):
             HVAC_STM["State"] = "Warming"
        elif(Temp > Limits["Temp_Lw_limit"]):
             HVAC_STM["State"] = "SB"
    HVAC_SB()



# Cots

def Heater_1_ON():
    pass

def Heater_2_ON():
    pass
def Heater_3_ON():
    pass
def Collar_1_OFF():
    pass
def Collar_2_OFF():
    pass
def Collar_3_OFF():
    pass
def Heater_1_OFF():
    pass
def Heater_2_OFF():
    pass
def Heater_3_OFF():
    pass
def Collar_1_ON():
    pass
def Collar_2_ON():
    pass
def Collar_3_ON():
    pass
'''
#testing
Hvac_Control_Runnable(26)
time.sleep(10)
Hvac_Control_Runnable(26)
time.sleep(10)
Hvac_Control_Runnable(26)
time.sleep(10)
Hvac_Control_Runnable(33)
time.sleep(10)
Hvac_Control_Runnable(33)
time.sleep(10)
Hvac_Control_Runnable(33)
time.sleep(10)
Hvac_Control_Runnable(33)
time.sleep(10)
Hvac_Control_Runnable(25)
time.sleep(10)
Hvac_Control_Runnable(25)
time.sleep(10)
Hvac_Control_Runnable(25)
time.sleep(10)
Hvac_Control_Runnable(25)
time.sleep(10)
Hvac_Control_Runnable(20)
time.sleep(10)
Hvac_Control_Runnable(20)
time.sleep(10)
Hvac_Control_Runnable(20)
time.sleep(10)
Hvac_Control_Runnable(20)
time.sleep(10)
Hvac_Control_Runnable(20)
time.sleep(10)
Hvac_Control_Runnable(20)
time.sleep(10)
Hvac_Control_Runnable(27)
time.sleep(10)
Hvac_Control_Runnable(27)
time.sleep(10)
Hvac_Control_Runnable(27)
time.sleep(10)
Hvac_Control_Runnable(27)
time.sleep(10)
Hvac_Control_Runnable(27)
time.sleep(10)
'''


Hvac_Control_Runnable(26)
print("state:",HVAC_STM["State"])
Hvac_Control_Runnable(19)
print("state:",HVAC_STM["State"])
Hvac_Control_Runnable(27)
print("state:",HVAC_STM["State"])
Hvac_Control_Runnable(40)
print("state:",HVAC_STM["State"])