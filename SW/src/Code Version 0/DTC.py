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

import time
import datetime
from datetime import datetime
from Sys_Data import Sys_DHT_DTC_sts

##################################################################
####               Define Global variable                     ####
##################################################################
Sys_DHT_DTC_Frq = {
    "DTC_1_Freq" : 0,
    "DTC_2_Freq" : 0,
    "DTC_3_Freq" : 0,
    "DTC_4_Freq" : 0,
    "DTC_5_Freq":0,
    "DTC_6_Freq":0,
    "DTC_7_Freq":0,
    "DTC_8_Freq":0,
    "DTC_9_Freq":0,
    "DTC_10_Freq":0,
    "DTC_11_Freq":0,
    "DTC_12_Freq":0,
}


DHT_Frequency_allow = 5


##################################################################
####                Function Definition                       ####
##################################################################


#######################################################################
# function name :  DHT_DIAG_Update                                    #
# Inputs :     dtc name                                               #
# Outputs :     none                                                  #
# Description :      check DTC to log                                 #
# Function Scope : ( External )                                       #
# Arch ID :                                                           #
#######################################################################

def DHT_DIAG_Update(DTC):
    # DTC_1 check
    if DTC == "DTC_1":
        if (Sys_DHT_DTC_Frq["DTC_1_Freq"]) < (DHT_Frequency_allow):
            Sys_DHT_DTC_sts["DTC_1"] = True
        else:
            Sys_DHT_DTC_Frq["DTC_1_Freq"]=(Sys_DHT_DTC_Frq["DTC_1_Freq"]+1)
    # DTC_2 check
    if DTC == "DTC_2":
        if (Sys_DHT_DTC_Frq["DTC_2_Freq"]) < (DHT_Frequency_allow):
            Sys_DHT_DTC_sts["DTC_2"] = True
        else:
            Sys_DHT_DTC_Frq["DTC_2_Freq"]=Sys_DHT_DTC_Frq["DTC_2_Freq"]+1
    # DTC_3 check
    if DTC == "DTC_3":
        if (Sys_DHT_DTC_Frq["DTC_3_Freq"]) > (DHT_Frequency_allow):
            Sys_DHT_DTC_sts["DTC_3"] = True
        else:
            Sys_DHT_DTC_Frq["DTC_3_Freq"]=Sys_DHT_DTC_Frq["DTC_3_Freq"]+1
    # DTC_4 check
    if DTC == "DTC_4":
        if (Sys_DHT_DTC_Frq["DTC_4_Freq"]) > (DHT_Frequency_allow):
            Sys_DHT_DTC_sts["DTC_4"] = True
        else:
            Sys_DHT_DTC_Frq["DTC_4_Freq"]=Sys_DHT_DTC_Frq["DTC_4_Freq"]+1
    # DTC_5 check
    if DTC == "DTC_5":
        if (Sys_DHT_DTC_Frq["DTC_5_Freq"]) > (DHT_Frequency_allow):
            Sys_DHT_DTC_sts["DTC_5"] = True
        else:
            Sys_DHT_DTC_Frq["DTC_5_Freq"]=Sys_DHT_DTC_Frq["DTC_5_Freq"]+1
    # DTC_6 check
    if DTC == "DTC_6":
        if Sys_DHT_DTC_Frq["DTC_6_Freq"] > DHT_Frequency_allow:
            Sys_DHT_DTC_sts["DTC_6"] = True
        else:
            Sys_DHT_DTC_Frq["DTC_6_Freq"]=Sys_DHT_DTC_Frq["DTC_6_Freq"]+1
    # DTC_7 check
    if DTC == "DTC_7":
        if Sys_DHT_DTC_Frq["DTC_7_Freq"] > DHT_Frequency_allow:
            Sys_DHT_DTC_sts["DTC_7"] = True
        else:
            Sys_DHT_DTC_Frq["DTC_7_Freq"]=Sys_DHT_DTC_Frq["DTC_7_Freq"]+1
    # DTC_8 check
    if DTC == "DTC_8":
        if Sys_DHT_DTC_Frq["DTC_8_Freq"] > DHT_Frequency_allow:
            Sys_DHT_DTC_sts["DTC_8"] = True
        else:
            Sys_DHT_DTC_sts["DTC_8_Freq"]=Sys_DHT_DTC_Frq["DTC_8_Freq"]+1
    # DTC_9 check
    if DTC == "DTC_9":
        if Sys_DHT_DTC_Frq["DTC_9_Freq"] > DHT_Frequency_allow:
            Sys_DHT_DTC_sts["DTC_9"] = True
        else:
            Sys_DHT_DTC_Frq["DTC_9_Freq"]=Sys_DHT_DTC_Frq["DTC_9_Freq"]+1
    # DTC_10 check
    if DTC == "DTC_10":
        if Sys_DHT_DTC_Frq["DTC_10_Freq"] > DHT_Frequency_allow:
            Sys_DHT_DTC_sts["DTC_10"] = True
        else:
            Sys_DHT_DTC_Frq["DTC_10_Freq"]=Sys_DHT_DTC_Frq["DTC_10_Freq"]+1
    # DTC_11 check
    if DTC == "DTC_11":
        if Sys_DHT_DTC_Frq["DTC_11_Freq"] > DHT_Frequency_allow:
            Sys_DHT_DTC_sts["DTC_11"] = True
        else:
            Sys_DHT_DTC_Frq["DTC_11_Freq"]=Sys_DHT_DTC_Frq["DTC_11_Freq"]+1
    # DTC_12 check
    if DTC == "DTC_12":
        if Sys_DHT_DTC_Frq["DTC_12_Freq"] > DHT_Frequency_allow:
            Sys_DHT_DTC_sts["DTC_1"] = True
        else:
            Sys_DHT_DTC_Frq["DTC_12_Freq"]=Sys_DHT_DTC_Frq["DTC_12_Freq"]+1
