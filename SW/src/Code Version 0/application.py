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

from urllib.request import urlopen
import xlsxwriter
from datetime import datetime
import pandas as pd
import openpyxl
from Sys_Data import Excel_data_frame ,Day_12_hour

from datetime import date
import datetime
import time


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
def is_internet_available():
    try:
        urlopen('https://google.com', timeout=1)
        return "Connected"
    except:
        return "Disconnected"



#######################################################################
# function name :                                                     #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
def Create_Excel_File(fimename):
    workbook = xlsxwriter.Workbook(fimename)
    worksheet = workbook.add_worksheet()
    workbook.close()

#######################################################################
# function name :                                                     #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
################# check Date Time and Update Data or Remove Data
def check_dat_changed():
    if Day_12_hour["Current_Day_time"] == Day_12_hour["Previous_Day_time"] :
        return False
    else:
        return True


#######################################################################
# function name :                                                     #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
def Update_date_time_Tracker():
    Day_12_hour["Current_Day_time"]= str(datetime.date.today())

#######################################################################
# function name :                                                     #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
def Update_Previous_Date():
    Day_12_hour["Previous_Day_time"] = Day_12_hour["Current_Day_time"]

#######################################################################
# function name :                                                     #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
def Remove_not_Requaired_data():
    Ammonia_sts["Ammonia"]=0

#######################################################################
# function name :                                                     #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
def check_Date_Time_and_Update_Data_Runnable():
    Update_date_time_Tracker()
    Date_Remove_Flag = check_dat_changed()
    Update_Previous_Date()
    Remove_not_Requaired_data()
    


