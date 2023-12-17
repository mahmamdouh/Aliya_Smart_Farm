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


##################################################################
####               Define Global variable                     ####
##################################################################
Frequency_allow = {
    "Freq_Max_Cnt" : 5,
}
##################################################################
####                      DHT_DTC                             ####
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

Sys_DHT_DTC_sts = {
    "DTC_1" : 0,
    "DTC_2" : 0,
    "DTC_3" : 0,
    "DTC_4" : 0,
    "DTC_5":0,
    "DTC_6":0,
    "DTC_7":0,
    "DTC_8_":0,
    "DTC_9":0,
    "DTC_10":0,
    "DTC_11":0,
    "DTC_12":0,
}




##################################################################
####                      MQ137_DTC                             ####
##################################################################
Sys_MQ137_DTC_Freq = {
    "DTC_33_Freq" : 0,
}

Sys_MQ137_DTC_sts = {
    "DTC_33" : 0,

}

##################################################################
####                      MQ135_DTC                             ####
##################################################################
Sys_MQ135_DTC_Freq = {
    "DTC_13_Freq" : 0,
    "DTC_14_Freq" : 0,

}

Sys_MQ135_DTC_sts = {
    "DTC_13" : 0,
    "DTC_14" : 0,
}

##################################################################
####                      Excel_DTC                             ####
##################################################################
Sys_Excel_DTC_Freq = {
    "DTC_17_Freq" : 0,
    "DTC_18_Freq" : 0,

}

Sys_Excel_DTC_sts = {
    "DTC_17" : 0,
    "DTC_18" : 0,
}


##################################################################
####                      Google_DTC                             ####
##################################################################
Sys_Google_DTC_Freq = {
    "DTC_19_Freq" : 0,
    "DTC_20_Freq" : 0,

}

Sys_Google_DTC_sts = {
    "DTC_19" : 0,
    "DTC_20" : 0,
}

##################################################################
####                      GPC_DTC                             ####
##################################################################

Sys_GPC_DTC_Freq = {
    "DTC_21_Freq" : 0,
    "DTC_22_Freq" : 0,
    "DTC_23_Freq" : 0,
}

Sys_GPC_DTC_sts = {
    "DTC_21" : 0,
    "DTC_22" : 0,
    "DTC_23" : 0,
}

##################################################################
####                      Internet_DTC                             ####
##################################################################
Sys_Internet_DTC_Freq = {
    "DTC_24_Freq" : 0,

}

Sys_Internet_DTC_sts = {
    "DTC_24" : 0,
}

##################################################################
####                      IP_CAM_DTC                             ####
##################################################################
Sys_IP_CAM_DTC_Freq = {
    "DTC_42_Freq" : 0,

}

Sys_IP_CAM_DTC_sts = {
    "DTC_42" : 0,
}

##################################################################
####                      Sensor_Board_DTC                             ####
##################################################################
Sys_Sensor_Board_DTC_Freq = {
    "DTC_36_Freq" : 0,
    "DTC_37_Freq" : 0,
    "DTC_38_Freq" : 0,
    "DTC_39_Freq" : 0,
    "DTC_40_Freq":0,
    "DTC_41_Freq":0,

}

Sys_Sensor_Board_DTC_sts = {
    "DTC_36" : 0,
    "DTC_37" : 0,
    "DTC_38" : 0,
    "DTC_39" : 0,
    "DTC_40":0,
    "DTC_41":0,
}

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
        if (Sys_DHT_DTC_Frq["DTC_1_Freq"]) < (Frequency_allow["Freq_Max_Cnt"]):
            Sys_DHT_DTC_sts["DTC_1"] = 1
        else:
            Sys_DHT_DTC_Frq["DTC_1_Freq"]=(Sys_DHT_DTC_Frq["DTC_1_Freq"]+1)
    # DTC_2 check
    if DTC == "DTC_2":
        if (Sys_DHT_DTC_Frq["DTC_2_Freq"]) < (Frequency_allow["Freq_Max_Cnt"]):
            Sys_DHT_DTC_sts["DTC_2"] = 1
        else:
            Sys_DHT_DTC_Frq["DTC_2_Freq"]=Sys_DHT_DTC_Frq["DTC_2_Freq"]+1
    # DTC_3 check
    if DTC == "DTC_3":
        if (Sys_DHT_DTC_Frq["DTC_3_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sys_DHT_DTC_sts["DTC_3"] = 1
        else:
            Sys_DHT_DTC_Frq["DTC_3_Freq"]=Sys_DHT_DTC_Frq["DTC_3_Freq"]+1
    # DTC_4 check
    if DTC == "DTC_4":
        if (Sys_DHT_DTC_Frq["DTC_4_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sys_DHT_DTC_sts["DTC_4"] = 1
        else:
            Sys_DHT_DTC_Frq["DTC_4_Freq"]=Sys_DHT_DTC_Frq["DTC_4_Freq"]+1
    # DTC_5 check
    if DTC == "DTC_5":
        if (Sys_DHT_DTC_Frq["DTC_5_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sys_DHT_DTC_sts["DTC_5"] = 1
        else:
            Sys_DHT_DTC_Frq["DTC_5_Freq"]=Sys_DHT_DTC_Frq["DTC_5_Freq"]+1
    # DTC_6 check
    if DTC == "DTC_6":
        if Sys_DHT_DTC_Frq["DTC_6_Freq"] > (Frequency_allow["Freq_Max_Cnt"]):
            Sys_DHT_DTC_sts["DTC_6"] = 1
        else:
            Sys_DHT_DTC_Frq["DTC_6_Freq"]=Sys_DHT_DTC_Frq["DTC_6_Freq"]+1
    # DTC_7 check
    if DTC == "DTC_7":
        if Sys_DHT_DTC_Frq["DTC_7_Freq"] > (Frequency_allow["Freq_Max_Cnt"]):
            Sys_DHT_DTC_sts["DTC_7"] = 1
        else:
            Sys_DHT_DTC_Frq["DTC_7_Freq"]=Sys_DHT_DTC_Frq["DTC_7_Freq"]+1
    # DTC_8 check
    if DTC == "DTC_8":
        if Sys_DHT_DTC_Frq["DTC_8_Freq"] > (Frequency_allow["Freq_Max_Cnt"]):
            Sys_DHT_DTC_sts["DTC_8"] = 1
        else:
            Sys_DHT_DTC_sts["DTC_8_Freq"]=Sys_DHT_DTC_Frq["DTC_8_Freq"]+1
    # DTC_9 check
    if DTC == "DTC_9":
        if Sys_DHT_DTC_Frq["DTC_9_Freq"] > (Frequency_allow["Freq_Max_Cnt"]):
            Sys_DHT_DTC_sts["DTC_9"] = 1
        else:
            Sys_DHT_DTC_Frq["DTC_9_Freq"]=Sys_DHT_DTC_Frq["DTC_9_Freq"]+1
    # DTC_10 check
    if DTC == "DTC_10":
        if Sys_DHT_DTC_Frq["DTC_10_Freq"] > (Frequency_allow["Freq_Max_Cnt"]):
            Sys_DHT_DTC_sts["DTC_10"] = 1
        else:
            Sys_DHT_DTC_Frq["DTC_10_Freq"]=Sys_DHT_DTC_Frq["DTC_10_Freq"]+1
    # DTC_11 check
    if DTC == "DTC_11":
        if Sys_DHT_DTC_Frq["DTC_11_Freq"] > (Frequency_allow["Freq_Max_Cnt"]):
            Sys_DHT_DTC_sts["DTC_11"] = 1
        else:
            Sys_DHT_DTC_Frq["DTC_11_Freq"]=Sys_DHT_DTC_Frq["DTC_11_Freq"]+1
    # DTC_12 check
    if DTC == "DTC_12":
        if Sys_DHT_DTC_Frq["DTC_12_Freq"] > (Frequency_allow["Freq_Max_Cnt"]):
            Sys_DHT_DTC_sts["DTC_1"] = 1
        else:
            Sys_DHT_DTC_Frq["DTC_12_Freq"]=Sys_DHT_DTC_Frq["DTC_12_Freq"]+1


def GPC_DTC_Update(DTC):
        # DTC_1 check
    if DTC == "DTC_21":
        if (Sys_GPC_DTC_Freq["DTC_21_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sys_GPC_DTC_sts["DTC_21"] = 1
        else:
            Sys_GPC_DTC_Freq["DTC_21_Freq"]=(Sys_GPC_DTC_Freq["DTC_21_Freq"]+1)
    # DTC_2 check
    if DTC == "DTC_22":
        if (Sys_GPC_DTC_Freq["DTC_22_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sys_GPC_DTC_sts["DTC_22"] = 1
        else:
            Sys_GPC_DTC_Freq["DTC_22_Freq"]=Sys_GPC_DTC_Freq["DTC_22_Freq"]+1
    # DTC_3 check
    if DTC == "DTC_23":
        if (Sys_GPC_DTC_Freq["DTC_23_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sys_GPC_DTC_sts["DTC_23"] = 1
        else:
            Sys_GPC_DTC_Freq["DTC_23_Freq"]=Sys_GPC_DTC_Freq["DTC_23_Freq"]+1


## code for trial SWIT 
def GET_GPC_Sts():
    print("DTC_21")
    print(Sys_GPC_DTC_sts["DTC_21"])
    print("DTC_22")
    print(Sys_GPC_DTC_sts["DTC_22"])
    print("DTC_23")
    print(Sys_GPC_DTC_sts["DTC_23"])