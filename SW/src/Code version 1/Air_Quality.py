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

import sys
import time
import datetime
from datetime import datetime
from Time_Control import Air_Timer_Start,Air_Time,Air_Timer_Cancel,Air_Timer_Check
from Sys_Data import Air_Quality_STM,Limits,Air_sts
from  IO_driver import Heater_1_OFF ,Heater_1_ON ,Heater_2_OFF ,Heater_2_ON ,Heater_3_OFF ,Heater_3_ON ,Collar_1_OFF ,Collar_1_ON ,Collar_2_OFF ,Collar_2_ON ,Collar_3_OFF ,Collar_3_ON

##################################################################
####               Define Global variable                     ####
##################################################################

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
def Air_Set_Limits(Ammonia , Air):
    # Temp limits
    Limits["Ammonia"] = Ammonia
    Limits["Air"] = Air



#######################################################################
# function name :                                                     #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
#Get temp limits
def Air_Get_Limits():
    return  Limits["Ammonia"] ,Limits["Air"]

#######################################################################
# function name :                                                     #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
#Get temp limits


def Air_Control_Runnable(Ammonia , Air):
    # State machine Control
    Air_STM_Run(Ammonia , Air)
    print("status to choose =",Air_Quality_STM["State"])
    if Air_Quality_STM["State"] == "SB":
        Air_SB()
    elif Air_Quality_STM["State"] == "Waiting":
        Air_Waiting(Ammonia , Air)
        Air_SB()
    elif Air_Quality_STM["State"] == "Open_Air":
        Air_Open_Air()
        print("volaaaa - open air          -----")
    #print("data and stm === end",Ammonia , Air,Air_Quality_STM)
def Air_STM_Run(Ammonia , Air):
    # State machine Control
    ## check SB mode
    if Air_Quality_STM["State"] == "SB":
        if(Ammonia > Limits["Ammonia"] or (Air > Limits["Air"])):
            Air_Quality_STM["State"] = "Waiting"
            Air_Quality_STM["Previous_state"]= "SB"
        else:
            #print("back to SB")
            Air_Quality_STM["State"] = "SB"
            Air_Quality_STM["Previous_state"]= "SB"
    #check open Air
    elif Air_Quality_STM["State"] == "Open_Air":
        if(Ammonia < Limits["Ammonia"] or Air < Limits["Air"]):
            Air_Quality_STM["State"] = "Waiting"
            Air_Quality_STM["Previous_state"]= "Open_Air"
        elif(Ammonia > Limits["Ammonia"] or Air > Limits["Air"]):
            Air_Quality_STM["State"]= "Open_Air" 
            
def Air_Open_Air():
    Heater_1_ON()
    Heater_2_ON()
    Heater_3_ON()
    Collar_1_ON()
    Collar_2_ON()
    Collar_3_ON()
    
def Air_SB():
    Heater_1_OFF()
    Heater_2_OFF()
    Heater_3_OFF()
    Collar_1_OFF()
    Collar_2_OFF()
    Collar_3_OFF()
    
def Air_Waiting(Ammonia , Air):
    Air_Timer_Check(10)
    #print("Air Time Flags",Air_Time)
    if Air_Time["Flag"] == True and Air_Time["Start_Flag"] == 0 :
        if(Ammonia < Limits["Ammonia"] and Air < Limits["Air"]):
            Air_Quality_STM["State"] = "SB"
            Air_Time["Flag"] = False
            Air_Quality_STM["Previous_state"]= "Waiting"
        elif(Ammonia > Limits["Ammonia"] or Air > Limits["Air"]):
            Air_Quality_STM["State"] = "Open_Air"
            Air_Time["Flag"] = False
            Air_Quality_STM["Previous_state"]= "Waiting"
    elif Air_Time["Flag"] == False and Air_Time["Start_Flag"] == 1 :
        Air_Quality_STM["State"] = "Waiting"
    elif Air_Time["Flag"] == False and Air_Time["Start_Flag"] == 0 :
        Air_Timer_Start()
        print("Timer start")
    elif Air_Time["Flag"] == True and Air_Time["Start_Flag"] == 1 :
        print("Some Thing Wrong =================================>")
'''
while True:
    Ammonia = 3
    Air = 20
    print("data",Ammonia,Air,Air_Quality_STM,Air_Time)
    Air_Control_Runnable(Ammonia,Air)
    print("data",Ammonia,Air,Air_Quality_STM,Air_Time)
    time.sleep(30)
    print("data ",Ammonia,Air,Air_Quality_STM,Air_Time)
    Air_Control_Runnable(Ammonia,Air)
    print("data",Ammonia,Air,Air_Quality_STM,Air_Time)
    time.sleep(30)
    ####################################################
    Ammonia = 3
    Air = 70
    print("data",Ammonia,Air,Air_Quality_STM,Air_Time)
    Air_Control_Runnable(Ammonia,Air)
    print("data",Ammonia,Air,Air_Quality_STM,Air_Time)
    time.sleep(30)
    print("data",Ammonia,Air,Air_Quality_STM,Air_Time)
    Air_Control_Runnable(Ammonia,Air)
    print("data",Ammonia,Air,Air_Quality_STM,Air_Time)
    time.sleep(30)
    ####################################################
    Ammonia = 3
    Air = 70
    print("data",Ammonia,Air,Air_Quality_STM,Air_Time)
    Air_Control_Runnable(Ammonia,Air)
    print("data",Ammonia,Air,Air_Quality_STM,Air_Time)
    time.sleep(30)
    print("data",Ammonia,Air,Air_Quality_STM,Air_Time)
    Air_Control_Runnable(Ammonia,Air)
    print("data",Ammonia,Air,Air_Quality_STM,Air_Time)
    time.sleep(30)
    
    ####################################################
    Ammonia = 50
    Air = 70
    print("data",Ammonia,Air,Air_Quality_STM,Air_Time)
    Air_Control_Runnable(Ammonia,Air)
    print("data",Ammonia,Air,Air_Quality_STM,Air_Time)
    time.sleep(30)
    print("data",Ammonia,Air,Air_Quality_STM,Air_Time)
    Air_Control_Runnable(Ammonia,Air)
    print("data",Ammonia,Air,Air_Quality_STM,Air_Time)
    time.sleep(30)
    
    ####################################################
    Ammonia = 50
    Air = 2
    print("data",Ammonia,Air,Air_Quality_STM,Air_Time)
    Air_Control_Runnable(Ammonia,Air)
    print("data",Ammonia,Air,Air_Quality_STM,Air_Time)
    time.sleep(30)
    print("data",Ammonia,Air,Air_Quality_STM,Air_Time)
    Air_Control_Runnable(Ammonia,Air)
    print("data",Ammonia,Air,Air_Quality_STM,Air_Time)
    time.sleep(30)
    
    ####################################################
    Ammonia = 3
    Air = 2
    print("data",Ammonia,Air,Air_Quality_STM,Air_Time)
    Air_Control_Runnable(Ammonia,Air)
    print("data",Ammonia,Air,Air_Quality_STM,Air_Time)
    time.sleep(30)
    print("data",Ammonia,Air,Air_Quality_STM,Air_Time)
    Air_Control_Runnable(Ammonia,Air)
    print("data",Ammonia,Air,Air_Quality_STM,Air_Time)
    time.sleep(30)
    
    print("End of Test Case =========================================")
    break
'''

def Update_Air_Status(Air):
    if Air > 0 and Air < 51:
        Air_sts["Condition"]="Good !"
    elif Air > 50 and Air < 100:
        Air_sts["Condition"]="Moderate"
    elif Air > 101 and Air < 150:
        Air_sts["Condition"]="poluted"
    elif Air > 151 and Air < 200:
        Air_sts["Condition"]="Unhealthy"
    elif Air > 201 and Air < 300:
        Air_sts["Condition"]="Very Unhealthy"
    elif Air > 301 :
        Air_sts["Condition"]="Hazard"
    