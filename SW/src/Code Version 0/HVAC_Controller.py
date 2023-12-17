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
from  IO_driver import Heater_1_OFF ,Heater_1_ON ,Heater_2_OFF ,Heater_2_ON ,Heater_3_OFF ,Heater_3_ON ,Collar_1_OFF ,Collar_1_ON ,Collar_2_OFF ,Collar_2_ON ,Collar_3_OFF ,Collar_3_ON

##################################################################
####               Define Global variable                     ####
##################################################################

# Temp limits
Temp_Lw_limit = 25
Temp_Up_limit = 30

# Hmid limits
Humid_Lw_limit = 10
Humid_Up_limit = 40
Limits = {
  "Temp_Lw_limit": 25,
  "Temp_Up_limit": 30,
  "Humid_Lw_limit": 10,
  "Humid_Up_limit": 40,
}
# temp now


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
def Hvac_control(Temp , Humid):
    # check temp exceed upper limit
    if(Temp < Limits["Temp_Lw_limit"] ):
        Heater_1_ON()
        Heater_2_ON()
        Heater_3_ON()
        Collar_1_OFF()
        Collar_2_OFF()
        Collar_3_OFF()

    elif (Temp >  Limits["Temp_Up_limit"]):
        Heater_1_OFF()
        Heater_2_OFF()
        Heater_3_OFF()
        Collar_1_ON()
        Collar_2_ON()
        Collar_3_ON()
    else :
        Heater_1_OFF()
        Heater_2_OFF()
        Heater_3_OFF()
        Collar_1_OFF()
        Collar_2_OFF()
        Collar_3_OFF()
        

    if(Humid > Limits["Humid_Up_limit"] ):
        # allarm of Humid
        print ("humis excced upper limit ")


    if (Humid < Limits["Humid_Lw_limit"]):
        # allarm of Humid
        print("humis decced lowwer limit ")





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





