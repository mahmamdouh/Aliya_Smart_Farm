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
####                      Sensor_Board_DTC                             ####
##################################################################
Sensor_Board_1_DTC_Frq = {
    "DTC_1_Freq" : 0,
    "DTC_2_Freq" : 0,
    "DTC_3_Freq" : 0,
    "DTC_4_Freq" : 0,
    "DTC_2_2_Freq": 0,
}

Sensor_Board_1_DTC_sts = {
    "DTC_1" : 0,
    "DTC_2" : 0,
    "DTC_3" : 0,
    "DTC_4" : 0,
    "DTC_2_2": 0,
}

# Sensor Board 2
Sensor_Board_2_DTC_Frq = {
    "DTC_5_Freq" : 0,
    "DTC_6_Freq" : 0,
    "DTC_7_Freq" : 0,
    "DTC_8_Freq" : 0,
    "DTC_6_2_Freq": 0,
}

Sensor_Board_2_DTC_sts = {
    "DTC_5" : 0,
    "DTC_6" : 0,
    "DTC_7" : 0,
    "DTC_8" : 0,
    "DTC_6_2": 0,
}
# Sensor Board 3
Sensor_Board_3_DTC_Frq = {
    "DTC_9_Freq" : 0,
    "DTC_10_Freq" : 0,
    "DTC_11_Freq" : 0,
    "DTC_12_Freq" : 0,
    "DTC_10_2_Freq": 0,
}

Sensor_Board_3_DTC_sts = {
    "DTC_9" : 0,
    "DTC_10" : 0,
    "DTC_11" : 0,
    "DTC_12" : 0,
    "DTC_10_2": 0,
}

# Sensor Board 4
Sensor_Board_4_DTC_Frq = {
    "DTC_13_Freq" : 0,
    "DTC_14_Freq" : 0,
    "DTC_15_Freq" : 0,
    "DTC_16_Freq" : 0,
    "DTC_14_2_Freq": 0,
}

Sensor_Board_4_DTC_sts = {
    "DTC_13" : 0,
    "DTC_14" : 0,
    "DTC_15" : 0,
    "DTC_16" : 0,
    "DTC_14_2": 0,
}

# Sensor Board 5
Sensor_Board_5_DTC_Frq = {
    "DTC_17_Freq" : 0,
    "DTC_18_Freq" : 0,
    "DTC_19_Freq" : 0,
    "DTC_20_Freq" : 0,
    "DTC_18_2_Freq": 0,
}

Sensor_Board_5_DTC_sts = {
    "DTC_17" : 0,
    "DTC_18" : 0,
    "DTC_19" : 0,
    "DTC_20" : 0,
    "DTC_18_2": 0,
}

# Sensor Board 6
Sensor_Board_6_DTC_Frq = {
    "DTC_21_Freq" : 0,
    "DTC_22_Freq" : 0,
    "DTC_23_Freq" : 0,
    "DTC_24_Freq" : 0,
    "DTC_22_2_Freq": 0,
}

Sensor_Board_6_DTC_sts = {
    "DTC_21" : 0,
    "DTC_22" : 0,
    "DTC_23" : 0,
    "DTC_24" : 0,
    "DTC_22_2": 0,
}
##################################################################
####                      Excel_DTC                             ####
##################################################################
Excel_DTC_Frq = {
    "DTC_25_Freq" : 0,
    "DTC_26_Freq" : 0,
}

Excel_DTC_sts = {
    "DTC_25" : 0,
    "DTC_26" : 0,
}
##################################################################
####                      Google_DTC                             ####
##################################################################
Google_DTC_Frq = {
    "DTC_27_Freq" : 0,
    "DTC_28_Freq" : 0,
}

Google_DTC_sts = {
    "DTC_27" : 0,
    "DTC_28" : 0,
}

##################################################################
####                      IP Cam_DTC                             ####
##################################################################
IP_CAM_DTC_Frq = {
    "DTC_33_Freq" : 0,
}

IP_CAM_DTC_sts = {
    "DTC_33" : 0,
}
##################################################################
####                      GPC_DTC                             ####
##################################################################
GPC_DTC_Frq = {
    "DTC_29_Freq" : 0,
    "DTC_30_Freq" : 0,
    "DTC_31_Freq": 0,
}

GPC_DTC_sts = {
    "DTC_29" : 0,
    "DTC_30" : 0,
    "DTC_31": 0,
}
##################################################################
####                      Internet Connection_DTC                             ####
##################################################################
Internet_DTC_Frq = {
    "DTC_32_Freq" : 0,
}

Internet_DTC_sts = {
    "DTC_32" : 0,
}
##################################################################
####                      Sensor_Data_Range_DTC                             ####
##################################################################
Sens_Data_Range_DTC_Frq = {
    "DTC_34_Freq" : 0,
    "DTC_35_Freq" : 0,
    "DTC_36_Freq": 0,
    "DTC_37_Freq": 0,
    "DTC_38_Freq": 0,
    "DTC_39_Freq": 0,
}

Sens_Data_Range_DTC_sts = {
    "DTC_34" : 0,
    "DTC_35" : 0,
    "DTC_36": 0,
    "DTC_37": 0,
    "DTC_38": 0,
    "DTC_39": 0,
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

def Sensor_Board_1_DIAG_Update(DTC):
    # DTC_1 check
    if DTC == "DTC_1":
        if (Sensor_Board_1_DTC_Frq["DTC_1_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_1_DTC_sts["DTC_1"] = 1
        else:
            Sensor_Board_1_DTC_Frq["DTC_1_Freq"]=(Sensor_Board_1_DTC_Frq["DTC_1_Freq"]+1)
    # DTC_2 check
    if DTC == "DTC_2":
        if (Sensor_Board_1_DTC_Frq["DTC_2_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_1_DTC_sts["DTC_2"] = 1
        else:
            Sensor_Board_1_DTC_Frq["DTC_2_Freq"]=Sensor_Board_1_DTC_Frq["DTC_2_Freq"]+1
    # DTC_3 check
    if DTC == "DTC_3":
        if (Sensor_Board_1_DTC_Frq["DTC_3_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_1_DTC_sts["DTC_3"] = 1
        else:
            Sensor_Board_1_DTC_Frq["DTC_3_Freq"]=Sensor_Board_1_DTC_Frq["DTC_3_Freq"]+1
    # DTC_4 check
    if DTC == "DTC_4":
        if (Sensor_Board_1_DTC_Frq["DTC_4_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_1_DTC_sts["DTC_4"] = 1
        else:
            Sensor_Board_1_DTC_Frq["DTC_4_Freq"]=Sensor_Board_1_DTC_Frq["DTC_4_Freq"]+1
    # DTC_2_2 check
    if DTC == "DTC_2_2":
        if (Sensor_Board_1_DTC_Frq["DTC_2_2_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_1_DTC_sts["DTC_2_2"] = 1
        else:
            Sensor_Board_1_DTC_Frq["DTC_2_2_Freq"]=Sensor_Board_1_DTC_Frq["DTC_2_2_Freq"]+1

def Sensor_Board_2_DIAG_Update(DTC):
    # DTC_5 check
    if DTC == "DTC_5":
        if (Sensor_Board_2_DTC_Frq["DTC_5_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_2_DTC_sts["DTC_5"] = 1
        else:
            Sensor_Board_2_DTC_Frq["DTC_5_Freq"] = (Sensor_Board_2_DTC_Frq["DTC_5_Freq"] + 1)
    # DTC_6 check
    if DTC == "DTC_6":
        if (Sensor_Board_2_DTC_Frq["DTC_6_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_2_DTC_sts["DTC_6"] = 1
        else:
            Sensor_Board_2_DTC_Frq["DTC_6_Freq"] = Sensor_Board_2_DTC_Frq["DTC_6_Freq"] + 1
    # DTC_7 check
    if DTC == "DTC_7":
        if (Sensor_Board_2_DTC_Frq["DTC_7_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_2_DTC_sts["DTC_7"] = 1
        else:
            Sensor_Board_2_DTC_Frq["DTC_7_Freq"] = Sensor_Board_2_DTC_Frq["DTC_7_Freq"] + 1
    # DTC_8 check
    if DTC == "DTC_8":
        if (Sensor_Board_2_DTC_Frq["DTC_8_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_2_DTC_sts["DTC_8"] = 1
        else:
            Sensor_Board_2_DTC_Frq["DTC_8_Freq"] = Sensor_Board_2_DTC_Frq["DTC_8_Freq"] + 1
    # DTC_6_2 check
    if DTC == "DTC_6_2":
        if (Sensor_Board_2_DTC_Frq["DTC_6_2_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_2_DTC_sts["DTC_6_2"] = 1
        else:
            Sensor_Board_2_DTC_Frq["DTC_6_2_Freq"] = Sensor_Board_2_DTC_Frq["DTC_6_2_Freq"] + 1

def Sensor_Board_3_DIAG_Update(DTC):
    # DTC_9 check
    if DTC == "DTC_9":
        if (Sensor_Board_3_DTC_Frq["DTC_9_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_3_DTC_sts["DTC_9"] = 1
        else:
            Sensor_Board_3_DTC_Frq["DTC_9_Freq"] = (Sensor_Board_3_DTC_Frq["DTC_9_Freq"] + 1)
    # DTC_10 check
    if DTC == "DTC_10":
        if (Sensor_Board_3_DTC_Frq["DTC_10_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_3_DTC_sts["DTC_10"] = 1
        else:
            Sensor_Board_3_DTC_Frq["DTC_10_Freq"] = Sensor_Board_3_DTC_Frq["DTC_10_Freq"] + 1
    # DTC_11 check
    if DTC == "DTC_11":
        if (Sensor_Board_3_DTC_Frq["DTC_11_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_3_DTC_sts["DTC_11"] = 1
        else:
            Sensor_Board_3_DTC_Frq["DTC_11_Freq"] = Sensor_Board_3_DTC_Frq["DTC_11_Freq"] + 1
    # DTC_12 check
    if DTC == "DTC_12":
        if (Sensor_Board_3_DTC_Frq["DTC_12_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_3_DTC_sts["DTC_12"] = 1
        else:
            Sensor_Board_3_DTC_Frq["DTC_12_Freq"] = Sensor_Board_3_DTC_Frq["DTC_12_Freq"] + 1
    # DTC_10_2 check
    if DTC == "DTC_10_2":
        if (Sensor_Board_3_DTC_Frq["DTC_10_2_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_3_DTC_sts["DTC_10_2"] = 1
        else:
            Sensor_Board_3_DTC_Frq["DTC_10_2_Freq"] = Sensor_Board_3_DTC_Frq["DTC_10_2_Freq"] + 1

def Sensor_Board_4_DIAG_Update(DTC):
    # DTC_13 check
    if DTC == "DTC_13":
        #print("Set_DTC 13 freq now ", Sensor_Board_4_DTC_Frq["DTC_13_Freq"])
        if (Sensor_Board_4_DTC_Frq["DTC_13_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_4_DTC_sts["DTC_13"] = 1
        else:
            Sensor_Board_4_DTC_Frq["DTC_13_Freq"] = (Sensor_Board_4_DTC_Frq["DTC_13_Freq"] + 1)
    # DTC_14 check
    if DTC == "DTC_14":
        if (Sensor_Board_4_DTC_Frq["DTC_14_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_4_DTC_sts["DTC_14"] = 1
        else:
            Sensor_Board_4_DTC_Frq["DTC_14_Freq"] = Sensor_Board_4_DTC_Frq["DTC_14_Freq"] + 1
    # DTC_15 check
    if DTC == "DTC_15":
        if (Sensor_Board_4_DTC_Frq["DTC_15_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_4_DTC_sts["DTC_15"] = 1
        else:
            Sensor_Board_4_DTC_Frq["DTC_15_Freq"] = Sensor_Board_4_DTC_Frq["DTC_15_Freq"] + 1
    # DTC_16 check
    if DTC == "DTC_16":
        if (Sensor_Board_4_DTC_Frq["DTC_16_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_4_DTC_sts["DTC_16"] = 1
        else:
            Sensor_Board_4_DTC_Frq["DTC_16_Freq"] = Sensor_Board_4_DTC_Frq["DTC_16_Freq"] + 1
    # DTC_14_2 check
    if DTC == "DTC_14_2":
        if (Sensor_Board_4_DTC_Frq["DTC_14_2_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_4_DTC_sts["DTC_14_2"] = 1
        else:
            Sensor_Board_4_DTC_Frq["DTC_14_2_Freq"] = Sensor_Board_4_DTC_Frq["DTC_14_2_Freq"] + 1

def Sensor_Board_5_DIAG_Update(DTC):
    # DTC_17 check
    if DTC == "DTC_17":
        if (Sensor_Board_5_DTC_Frq["DTC_17_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_5_DTC_sts["DTC_17"] = 1
        else:
            Sensor_Board_5_DTC_Frq["DTC_17_Freq"] = (Sensor_Board_5_DTC_Frq["DTC_17_Freq"] + 1)
    # DTC_18 check
    if DTC == "DTC_18":
        if (Sensor_Board_5_DTC_Frq["DTC_18_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_5_DTC_sts["DTC_18"] = 1
        else:
            Sensor_Board_5_DTC_Frq["DTC_18_Freq"] = Sensor_Board_5_DTC_Frq["DTC_18_Freq"] + 1
    # DTC_19 check
    if DTC == "DTC_19":
        if (Sensor_Board_5_DTC_Frq["DTC_19_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_5_DTC_sts["DTC_19"] = 1
        else:
            Sensor_Board_5_DTC_Frq["DTC_19_Freq"] = Sensor_Board_5_DTC_Frq["DTC_19_Freq"] + 1
    # DTC_20 check
    if DTC == "DTC_20":
        if (Sensor_Board_5_DTC_Frq["DTC_20_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_5_DTC_sts["DTC_20"] = 1
        else:
            Sensor_Board_5_DTC_Frq["DTC_20_Freq"] = Sensor_Board_5_DTC_Frq["DTC_20_Freq"] + 1
    # DTC_18_2 check
    if DTC == "DTC_18_2":
        if (Sensor_Board_5_DTC_Frq["DTC_18_2_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_5_DTC_sts["DTC_18_2"] = 1
        else:
            Sensor_Board_5_DTC_Frq["DTC_18_2_Freq"] = Sensor_Board_5_DTC_Frq["DTC_18_2_Freq"] + 1

def Sensor_Board_6_DIAG_Update(DTC):
    # DTC_21 check
    if DTC == "DTC_21":
        if (Sensor_Board_6_DTC_Frq["DTC_21_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_6_DTC_sts["DTC_21"] = 1
        else:
            Sensor_Board_6_DTC_Frq["DTC_21_Freq"] = (Sensor_Board_6_DTC_Frq["DTC_21_Freq"] + 1)
    # DTC_22 check
    if DTC == "DTC_22":
        if (Sensor_Board_6_DTC_Frq["DTC_22_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_6_DTC_sts["DTC_22"] = 1
        else:
            Sensor_Board_6_DTC_Frq["DTC_22_Freq"] = Sensor_Board_6_DTC_Frq["DTC_22_Freq"] + 1
    # DTC_23 check
    if DTC == "DTC_23":
        if (Sensor_Board_6_DTC_Frq["DTC_23_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_6_DTC_sts["DTC_23"] = 1
        else:
            Sensor_Board_6_DTC_Frq["DTC_23_Freq"] = Sensor_Board_6_DTC_Frq["DTC_23_Freq"] + 1
    # DTC_24 check
    if DTC == "DTC_24":
        if (Sensor_Board_6_DTC_Frq["DTC_24_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_6_DTC_sts["DTC_24"] = 1
        else:
            Sensor_Board_6_DTC_Frq["DTC_24_Freq"] = Sensor_Board_6_DTC_Frq["DTC_24_Freq"] + 1
    # DTC_22_2 check
    if DTC == "DTC_22_2":
        if (Sensor_Board_6_DTC_Frq["DTC_22_2_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sensor_Board_6_DTC_sts["DTC_22_2"] = 1
        else:
            Sensor_Board_6_DTC_Frq["DTC_22_2_Freq"] = Sensor_Board_6_DTC_Frq["DTC_22_2_Freq"] + 1

def Excel_DIAG_Update(DTC):
    # DTC_25 check
    if DTC == "DTC_25":
        if (Excel_DTC_Frq["DTC_25_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Excel_DTC_sts["DTC_25"] = 1
        else:
            Excel_DTC_Frq["DTC_25_Freq"] = (Excel_DTC_Frq["DTC_25_Freq"] + 1)
    # DTC_26 check
    if DTC == "DTC_26":
        if (Excel_DTC_Frq["DTC_26_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Excel_DTC_sts["DTC_26"] = 1
        else:
            Excel_DTC_Frq["DTC_26_Freq"] = Excel_DTC_Frq["DTC_26_Freq"] + 1


def Google_DIAG_Update(DTC):
    # DTC_27 check
    if DTC == "DTC_27":
        if (Google_DTC_Frq["DTC_27_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Google_DTC_sts["DTC_27"] = 1
        else:
            Google_DTC_Frq["DTC_27_Freq"] = (Google_DTC_Frq["DTC_27_Freq"] + 1)
    # DTC_28 check
    if DTC == "DTC_28":
        if (Google_DTC_Frq["DTC_28_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Google_DTC_sts["DTC_28"] = 1
        else:
            Google_DTC_Frq["DTC_28_Freq"] = Google_DTC_Frq["DTC_28_Freq"] + 1


def IP_CAM_DIAG_Update(DTC):
    # DTC_33 check
    if DTC == "DTC_33":
        if (IP_CAM_DTC_Frq["DTC_33_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            IP_CAM_DTC_sts["DTC_33"] = 1
        else:
            IP_CAM_DTC_Frq["DTC_33_Freq"] = (IP_CAM_DTC_Frq["DTC_33_Freq"] + 1)


def GPC_DIAG_Update(DTC):
    # DTC_29 check
    if DTC == "DTC_29":
        if (GPC_DTC_Frq["DTC_29_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            GPC_DTC_sts["DTC_29"] = 1
        else:
            GPC_DTC_Frq["DTC_29_Freq"] = (GPC_DTC_Frq["DTC_29_Freq"] + 1)
    # DTC_30 check
    if DTC == "DTC_30":
        if (GPC_DTC_Frq["DTC_30_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            GPC_DTC_sts["DTC_30"] = 1
        else:
            GPC_DTC_Frq["DTC_30_Freq"] = GPC_DTC_Frq["DTC_30_Freq"] + 1
    # DTC_31 check
    if DTC == "DTC_31":
        if (GPC_DTC_Frq["DTC_31_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            GPC_DTC_sts["DTC_31"] = 1
        else:
            GPC_DTC_Frq["DTC_31_Freq"] = GPC_DTC_Frq["DTC_31_Freq"] + 1

def Internet_DIAG_Update(DTC):
    # DTC_32 check
    if DTC == "DTC_32":
        if (Internet_DTC_Frq["DTC_32_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Internet_DTC_sts["DTC_32"] = 1
        else:
            Internet_DTC_Frq["DTC_32_Freq"] = (Internet_DTC_Frq["DTC_32_Freq"] + 1)


def Sens_Data_Range_DIAG_Update(DTC):
    # DTC_34 check
    if DTC == "DTC_34":
        if (Sens_Data_Range_DTC_Frq["DTC_34_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sens_Data_Range_DTC_sts["DTC_34"] = 1
        else:
            Sens_Data_Range_DTC_Frq["DTC_34_Freq"] = (Sens_Data_Range_DTC_Frq["DTC_34_Freq"] + 1)
    # DTC_35 check
    if DTC == "DTC_35":
        if (Sens_Data_Range_DTC_Frq["DTC_35_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sens_Data_Range_DTC_sts["DTC_35"] = 1
        else:
            Sens_Data_Range_DTC_Frq["DTC_35_Freq"] = Sens_Data_Range_DTC_Frq["DTC_35_Freq"] + 1
    # DTC_36 check
    if DTC == "DTC_36":
        if (Sens_Data_Range_DTC_Frq["DTC_36_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sens_Data_Range_DTC_sts["DTC_36"] = 1
        else:
            Sens_Data_Range_DTC_Frq["DTC_36_Freq"] = Sens_Data_Range_DTC_Frq["DTC_36_Freq"] + 1
    # DTC_37 check
    if DTC == "DTC_37":
        if (Sens_Data_Range_DTC_Frq["DTC_37_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sens_Data_Range_DTC_sts["DTC_37"] = 1
        else:
            Sens_Data_Range_DTC_Frq["DTC_37_Freq"] = (Sens_Data_Range_DTC_Frq["DTC_37_Freq"] + 1)
    # DTC_38 check
    if DTC == "DTC_38":
        if (Sens_Data_Range_DTC_Frq["DTC_38_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sens_Data_Range_DTC_sts["DTC_38"] = 1
        else:
            Sens_Data_Range_DTC_Frq["DTC_38_Freq"] = Sens_Data_Range_DTC_Frq["DTC_38_Freq"] + 1
    # DTC_39 check
    if DTC == "DTC_39":
        if (Sens_Data_Range_DTC_Frq["DTC_39_Freq"]) > (Frequency_allow["Freq_Max_Cnt"]):
            Sens_Data_Range_DTC_sts["DTC_39"] = 1
        else:
            Sens_Data_Range_DTC_Frq["DTC_39_Freq"] = Sens_Data_Range_DTC_Frq["DTC_39_Freq"] + 1


def Clear_Dtc():
    Sensor_Board_1_DTC_sts["DTC_1"] = 0
    Sensor_Board_1_DTC_sts["DTC_2"] = 0
    Sensor_Board_1_DTC_sts["DTC_3"] = 0
    Sensor_Board_1_DTC_sts["DTC_4"] = 0
    Sensor_Board_2_DTC_sts["DTC_5"] = 0
    Sensor_Board_2_DTC_sts["DTC_6"] = 0
    Sensor_Board_2_DTC_sts["DTC_7"] = 0
    Sensor_Board_2_DTC_sts["DTC_8"] = 0
    Sensor_Board_3_DTC_sts["DTC_9"] = 0
    Sensor_Board_3_DTC_sts["DTC_10"] = 0
    Sensor_Board_3_DTC_sts["DTC_11"] = 0
    Sensor_Board_3_DTC_sts["DTC_12"] = 0
    Sensor_Board_4_DTC_sts["DTC_13"] = 0
    Sensor_Board_4_DTC_sts["DTC_14"] = 0
    Sensor_Board_4_DTC_sts["DTC_15"] = 0
    Sensor_Board_4_DTC_sts["DTC_16"] = 0
    Sensor_Board_5_DTC_sts["DTC_17"] = 0
    Sensor_Board_5_DTC_sts["DTC_18"] = 0
    Sensor_Board_5_DTC_sts["DTC_19"] = 0
    Sensor_Board_5_DTC_sts["DTC_20"] = 0
    Sensor_Board_6_DTC_sts["DTC_21"] = 0
    Sensor_Board_6_DTC_sts["DTC_22"] = 0
    Sensor_Board_6_DTC_sts["DTC_23"] = 0
    Sensor_Board_6_DTC_sts["DTC_24"] = 0
    Excel_DTC_sts["DTC_25"] = 0
    Excel_DTC_sts["DTC_26"] = 0
    Google_DTC_sts["DTC_27"] = 0
    Google_DTC_sts["DTC_28"] = 0
    IP_CAM_DTC_sts["DTC_33"] = 0
    GPC_DTC_sts["DTC_29"] = 0
    GPC_DTC_sts["DTC_30"] = 0
    GPC_DTC_sts["DTC_31"] = 0
    Internet_DTC_sts["DTC_32"] = 0
    Sens_Data_Range_DTC_sts["DTC_34"] = 0
    Sens_Data_Range_DTC_sts["DTC_35"] = 0
    Sens_Data_Range_DTC_sts["DTC_36"] = 0
    Sens_Data_Range_DTC_sts["DTC_37"] = 0
    Sens_Data_Range_DTC_sts["DTC_38"] = 0
    Sens_Data_Range_DTC_sts["DTC_39"] = 0

def Get_DTC_Sts():
    DTC_List = []
    DTC_List.append(str(Sensor_Board_1_DTC_sts["DTC_1"]))
    DTC_List.append(str(Sensor_Board_1_DTC_sts["DTC_2"]))
    DTC_List.append(str(Sensor_Board_1_DTC_sts["DTC_3"]))
    DTC_List.append(str(Sensor_Board_1_DTC_sts["DTC_4"]))
    DTC_List.append(str(Sensor_Board_2_DTC_sts["DTC_5"]))
    DTC_List.append(str(Sensor_Board_2_DTC_sts["DTC_6"]))
    DTC_List.append(str(Sensor_Board_2_DTC_sts["DTC_7"]))
    DTC_List.append(str(Sensor_Board_2_DTC_sts["DTC_8"]))
    DTC_List.append(str(Sensor_Board_3_DTC_sts["DTC_9"]))
    DTC_List.append(str(Sensor_Board_3_DTC_sts["DTC_10"]))
    DTC_List.append(str(Sensor_Board_3_DTC_sts["DTC_11"]))
    DTC_List.append(str(Sensor_Board_3_DTC_sts["DTC_12"]))
    DTC_List.append(str(Sensor_Board_4_DTC_sts["DTC_13"]))
    DTC_List.append(str(Sensor_Board_4_DTC_sts["DTC_14"]))
    DTC_List.append(str(Sensor_Board_4_DTC_sts["DTC_15"]))
    DTC_List.append(str(Sensor_Board_4_DTC_sts["DTC_16"]))
    DTC_List.append(str(Sensor_Board_5_DTC_sts["DTC_17"]))
    DTC_List.append(str(Sensor_Board_5_DTC_sts["DTC_18"]))
    DTC_List.append(str(Sensor_Board_5_DTC_sts["DTC_19"]))
    DTC_List.append(str(Sensor_Board_5_DTC_sts["DTC_20"]))
    DTC_List.append(str(Sensor_Board_6_DTC_sts["DTC_21"]))
    DTC_List.append(str(Sensor_Board_6_DTC_sts["DTC_22"]))
    DTC_List.append(str(Sensor_Board_6_DTC_sts["DTC_23"]))
    DTC_List.append(str(Sensor_Board_6_DTC_sts["DTC_24"]))
    DTC_List.append(str(Excel_DTC_sts["DTC_25"]))
    DTC_List.append(str(Excel_DTC_sts["DTC_26"]))
    DTC_List.append(str(Google_DTC_sts["DTC_27"]))
    DTC_List.append(str(Google_DTC_sts["DTC_28"]))
    DTC_List.append(str(IP_CAM_DTC_sts["DTC_33"]))
    DTC_List.append(str(GPC_DTC_sts["DTC_29"]))
    DTC_List.append(str(GPC_DTC_sts["DTC_30"]))
    DTC_List.append(str(GPC_DTC_sts["DTC_31"]))
    DTC_List.append(str(Internet_DTC_sts["DTC_32"]))
    DTC_List.append(str(Sens_Data_Range_DTC_sts["DTC_34"]))
    DTC_List.append(str(Sens_Data_Range_DTC_sts["DTC_35"]))
    DTC_List.append(str(Sens_Data_Range_DTC_sts["DTC_36"]))
    DTC_List.append(str(Sens_Data_Range_DTC_sts["DTC_37"]))
    DTC_List.append(str(Sens_Data_Range_DTC_sts["DTC_38"]))
    DTC_List.append(str(Sens_Data_Range_DTC_sts["DTC_39"]))
    return(DTC_List)

def Init_Update_DTC_Config_Sts(Input_List):
    Sensor_Board_1_DTC_sts["DTC_1"]=Input_List[0]
    Sensor_Board_1_DTC_sts["DTC_2"]=Input_List[1]
    Sensor_Board_1_DTC_sts["DTC_3"]=Input_List[2]
    Sensor_Board_1_DTC_sts["DTC_4"]=Input_List[3]
    Sensor_Board_2_DTC_sts["DTC_5"]=Input_List[4]
    Sensor_Board_2_DTC_sts["DTC_6"]=Input_List[5]
    Sensor_Board_2_DTC_sts["DTC_7"]=Input_List[6]
    Sensor_Board_2_DTC_sts["DTC_8"]=Input_List[7]
    Sensor_Board_3_DTC_sts["DTC_9"]=Input_List[8]
    Sensor_Board_3_DTC_sts["DTC_10"]=Input_List[9]
    Sensor_Board_3_DTC_sts["DTC_11"]=Input_List[10]
    Sensor_Board_3_DTC_sts["DTC_12"]=Input_List[11]
    Sensor_Board_4_DTC_sts["DTC_13"]=Input_List[12]
    Sensor_Board_4_DTC_sts["DTC_14"]=Input_List[13]
    Sensor_Board_4_DTC_sts["DTC_15"]=Input_List[14]
    Sensor_Board_4_DTC_sts["DTC_16"]=Input_List[15]
    Sensor_Board_5_DTC_sts["DTC_17"]=Input_List[16]
    Sensor_Board_5_DTC_sts["DTC_18"]=Input_List[17]
    Sensor_Board_5_DTC_sts["DTC_19"]=Input_List[18]
    Sensor_Board_5_DTC_sts["DTC_20"]=Input_List[19]
    Sensor_Board_6_DTC_sts["DTC_21"]=Input_List[20]
    Sensor_Board_6_DTC_sts["DTC_22"]=Input_List[21]
    Sensor_Board_6_DTC_sts["DTC_23"]=Input_List[22]
    Sensor_Board_6_DTC_sts["DTC_24"]=Input_List[23]
    Excel_DTC_sts["DTC_25"]=Input_List[24]
    Excel_DTC_sts["DTC_26"]=Input_List[25]
    Google_DTC_sts["DTC_27"]=Input_List[26]
    Google_DTC_sts["DTC_28"]=Input_List[27]
    IP_CAM_DTC_sts["DTC_33"]=Input_List[32]
    GPC_DTC_sts["DTC_29"]=Input_List[28]
    GPC_DTC_sts["DTC_30"]=Input_List[29]
    GPC_DTC_sts["DTC_31"]=Input_List[30]
    Internet_DTC_sts["DTC_32"]=Input_List[31]
    Sens_Data_Range_DTC_sts["DTC_34"]=Input_List[32]
    Sens_Data_Range_DTC_sts["DTC_35"]=Input_List[34]
    Sens_Data_Range_DTC_sts["DTC_36"]=Input_List[35]
    Sens_Data_Range_DTC_sts["DTC_37"]=Input_List[36]
    Sens_Data_Range_DTC_sts["DTC_38"]=Input_List[37]
    Sens_Data_Range_DTC_sts["DTC_39"]=Input_List[38]
    
    
    
# testing
