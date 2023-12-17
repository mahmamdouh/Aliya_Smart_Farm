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
##	component name : Application         						##
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
from Sys_Data import Excel_data_frame,Room_temp_sts,Ammonia_sts,Air_sts,Room_Humid_sts,Set_Today,Update_Day,Excel_Sheet,Excel_data_frame,min_Temp_limit_stamp,max_Temp_limit_stamp,Get_Date,time_stamp,Room_temp,sys_status,Excel_data_frame
from Sensor_Board_Handler import Sensor_Board_Handler_Runnable
from google_spreadsheet import Google_sheet_send_data ,Google_Sheets_Runnable
from Excel_Local_data import Write_to_Excel_data
from datetime import date
import datetime
import time
from Correct_Filter import Correct_factor_runable
##################################################################
####               Define Global variable                     ####
##################################################################


##################################################################
####                Function Definition                       ####
##################################################################
##################################################################

#######################################################################
# function name : App Main_Function
# Inputs :      NO
# Outputs :      NO
# Description : This Function Get all data from Sensor board
#               ( Temprature , Humidity and Air Quality
#               and check valid data and Log DTC of there is
#               and Update Global Data
# Function Scope : ( Local - External )
# Arch ID :
#######################################################################
def App_Main():
    Temprature,Humidity = Sensors_Handler()
    time_stmp = Get_Date()
    sys_status["application"] = "Running"
    if Temprature != 0:
        min_Temp_limit_stamp.append(Limits["Temp_Lw_limit"])
        max_Temp_limit_stamp.append(Limits["Temp_Up_limit"])
        Room_temp.append(Temprature)
        time_stamp.append(time_stmp)
        ## send data to spread sheet
        sys_status["internet_connection"] = is_internet_available()
        if sys_status["internet_connection"] == "Connected":
            Google_Sheets_Runnable(Temprature, Humidity, 0)
        ## Local Excel update data
        Excel_data_frame.loc[len(Excel_data_frame.index)] = [int(time_stmp), int(Temprature)]
        Excel_Data_Handler()




#######################################################################
# function name : App initialization
# Inputs :      NO
# Outputs :      NO
# Description : This Function Get all data from Sensor board
#               ( Temprature , Humidity and Air Quality
#               and check valid data and Log DTC of there is
#               and Update Global Data
# Function Scope : ( Local - External )
# Arch ID :
#######################################################################
def App_Init():
    # create Startup Sheet
    Local_Excel_File = str(datetime.date.today()) + '.xlsx'
    Create_Excel_File(("Data/"+Local_Excel_File))
    Excel_Sheet["Sheet_Name"]=("Data/"+Local_Excel_File)
    HVAC_Handler()
    return

#######################################################################
# function name : Sensors_Handler                                    
# Inputs :      NO                                                      
# Outputs :      NO                                                     
# Description : This Function Get all data from Sensor board 
#               ( Temprature , Humidity and Air Quality
#               and check valid data and Log DTC of there is 
#               and Update Global Data                                                      
# Function Scope : ( Local - External )                               
# Arch ID :                                                           
#######################################################################
def Sensors_Handler():
	TempFalse,HumidFalse,Ammonia = Sensor_Board_Handler_Runnable([5,6],"Ammonia")
    values = Ammonia.values()
    total_Ammonia = sum(values)
    Ammonia_sts["Ammonia"] = total_Ammonia
	TempFalse,HumidFalse,Air_Quality =Sensor_Board_Handler_Runnable([3,6],"AIR")
    values = Air_Quality.values()
    total_Air_Quality = sum(values)
    Air_sts["AirQuality"]=(total_Air_Quality/2)
    Temprature , Humidity ,DataFalse = Sensor_Board_Handler_Runnable([3,6],"Normal")
    Tamp_Correct_Values = Correct_factor_runable(Temprature,2)
    values = Tamp_Correct_Values.values()
    total_Tamp_Correct_Values = sum(values)
    Room_temp_sts["Room_temp"] = (total_Tamp_Correct_Values / len(Tamp_Correct_Values))
    values = Humidity.values()
    total_Humidity = sum(values)
    Room_Humid_sts["Room_Humid"]= (total_Humidity/6)
    Temprate1=float(Room_temp_sts["Room_temp"])
    Humidity1= float(Room_Humid_sts["Room_Humid"])
    return (Temprate1,Humidity1)

#######################################################################
# function name : Air_Quality_Handler                                    
# Inputs :       Ammonia , Air                                                     
# Outputs :        NO                                                   
# Description :   this function Control of Air conditioning depending on 
#                 ammonia status and Air quality status                                                     
# Function Scope : ( Local - External )                               
# Arch ID :                                                           
#######################################################################
def Air_Quality_Handler():
	
	return 

#######################################################################
# function name : Hazzard_Handler                                    
# Inputs :        NO                                                 
# Outputs :       NO                                                      
# Description :   This Function Trigger Buzzer larm if there is any Critical 
#                  Issue happened                                                       
# Function Scope : ( Local - External )                                
# Arch ID :                                                           
#######################################################################
def Hazzard_Handler():
	
	return 

#######################################################################
# function name : Excel_Data_Handler                                    
# Inputs :           Sheet Name , Data as a structure                                              
# Outputs :          NO                                                 
# Description :     This Function Store readig Data to Excel sheet 
#                   and generate new Excel sheet if need                                                 
# Function Scope : ( Local - External )                               
# Arch ID :                                                           
#######################################################################
def Excel_Data_Handler():
	flag = Update_Day()
    if flag:
        Local_Excel_File = str(datetime.date.today()) + '.xlsx'
        Create_Excel_File(("Data/" + Local_Excel_File))
        Excel_Sheet["Sheet_Name"] = ("Data/" + Local_Excel_File)
    Write_to_Excel_data(Excel_data_frame,Excel_Sheet["Sheet_Name"])
	return


#######################################################################
# function name : Time Handller
# Inputs :           Sheet Name , Data as a structure
# Outputs :          NO
# Description :     This Function Store readig Data to Excel sheet
#                   and generate new Excel sheet if need
# Function Scope : ( Local - External )
# Arch ID :
#######################################################################
def Time_Handler():
    Set_Today()
    Flag = Update_Day()
    return Flag
#######################################################################
# function name : Server_Handler                                    
# Inputs :           Data (all type of Data ) " Not defned yet                                                
# Outputs :          CRC_Flag , Command                                          
# Description :      This function Store all data to server and check if
#                    there is any Command comming from Client                                            
# Function Scope : ( Local - External )                               
# Arch ID :                                                           
#######################################################################
def Server_Handler():
	
	return 

#######################################################################
# function name : Food_Handler                                    
# Inputs :        Day_Number , Head Count                                                 
# Outputs :       NO                                                    
# Description :    This Function control of feeding system                                                    
# Function Scope : ( Local - External )                               
# Arch ID :                                                           
#######################################################################
def Food_Handler():
	
	return 




#######################################################################
# function name : Scaler_Handler                                    
# Inputs :        Rading Numbers                                              
# Outputs :       This function handel operation of measuring weighte 
#                 interacting with customer                                                     
# Description :                                                       
# Function Scope : ( Local - External )                               
# Arch ID :                                                           
#######################################################################
def Scaler_Handler():
	
	return 

#######################################################################
# function name : Configuration_Handler                                    
# Inputs :         config Data                                                    
# Outputs :         NO                                                  
# Description :    This function Update Configurtion Data in TXT File                                                    
# Function Scope : ( Local - External )                               
# Arch ID :                                                           
#######################################################################
def Configuration_Handler():
	
	return 

#######################################################################
# function name : HVAC_Handler                                    
# Inputs :        Temp                                                 
# Outputs :      NO                                                        
# Description :    This function Control of Heating and cooling of room 
#                   Pending on current temprature                                                        
# Function Scope : ( Local - External )                               
# Arch ID :                                                           
#######################################################################
def HVAC_Handler():
    Hvac_Control_Runnable(Room_temp_sts["Room_temp"])
	return 



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