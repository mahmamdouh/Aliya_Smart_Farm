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
from Sys_Data import Data,Alarm,HVAC_Active_Time,HVAC_sys_sts,Limits,HVAC_STM,sys_status,Air_Quality_STM,Room_temp_sts,Room_Humid_sts,Ammonia_sts,Air_sts,Head_count_sts,Operator_HVAC_sys_sts,Excel_data_frame,worksheet,Excel_Sheet,previous,Window_2_status,Day_hour,Get_Date,time_to_sleep,Set_Today,Update_Day,Day_12_hour,Update_12hur
from Sensor_Board_Handler import Sensor_Board_Handler_Runnable
from google_spreadsheet import Google_sheet_send_data ,Google_sheet_Get_data
from Excel_Local_data import Write_to_Excel_data
from datetime import date
import datetime
import time
from HVAC_Controller import Hvac_Control_Runnable,Hvac_Set_Limits,Hvac_Get_Limits ,Limits
from Correct_Filter import Correct_factor_runable
from Air_Quality import Update_Air_Status,Air_Control_Runnable
from Configer import config_Update_data,read_Data_Config
from CPU_Monitor import Check_PI_Status
from DTC import *
from DTC_Config import read_DTC_Config ,config_Update_DTC_data
##################################################################
####               Define Global variable                     ####
##################################################################
global Room_temprate
global time_slice
global min_Temp_limit_stamp
global max_Temp_limit_stamp
Room_temprate =[]
time_slice =[]
min_Temp_limit_stamp =[]
max_Temp_limit_stamp =[]

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
    global Room_temprate
    global time_slice
    global min_Temp_limit_stamp
    global max_Temp_limit_stamp
    print("Start Application")
    sys_status["application"] = "Running"
    Temprature,Humidity = Sensors_Handler()
    time_stmp = Get_Date()   
    if Temprature != 0:
        print("Save Sensor Data")
        FLG = 1
        min_Temp_limit_stamp.append(Limits["Temp_Lw_limit"])
        max_Temp_limit_stamp.append(Limits["Temp_Up_limit"])
        Room_temprate.append(Temprature)
        time_slice.append(time_stmp)
        ## send data to spread sheet
        print("Save Sensor Data in Google")
        sys_status["internet_connection"] = is_internet_available()
        if sys_status["internet_connection"] == "Connected":
            Google_sheet_send_data(Temprature, Humidity, Ammonia_sts["Ammonia"],Air_sts["AirQuality"],HVAC_STM["State"],Air_Quality_STM["State"])
        ## Local Excel update data
            print("Save Sensor Data in Excel")
        Excel_data_frame.loc[len(Excel_data_frame.index)] = [float(time_stmp), int(Temprature),int(Humidity),Ammonia_sts["Ammonia"],Air_sts["AirQuality"],HVAC_STM["State"],Air_Quality_STM["State"]]
        Excel_Data_Handler()
    HVAC_Handler()
    if (Time_Handler()):
        print("Day changed")
        Room_temprate=[]
        time_slice=[]
        min_Temp_limit_stamp=[]
        max_Temp_limit_stamp=[]
        Clear = 1
        Data["Age"] = str(int(Data["Age"]) +1)

    if Data["Updte_Flag"] == 1:
        #Get_Config_Data()
        Data["Updte_Flag"] = 0

    #Update Configuration
    Update_Config_Data()

    ##Air Control Runnable
    #Air_Control_Runnable(Ammonia_sts["Ammonia"],Air_sts["AirQuality"])

    ## check Data Request From Mobile app
    data = Google_sheet_Get_data()
    if data:
        Limits["Temp_Lw_limit"]=float(data[0])
        Limits["Temp_Up_limit"]=float(data[1])
        Limits["Ammonia"]=float(data[2])
    else:
        pass
    #CPU Monitor
    print("Check_PI_Status")
    Check_PI_Status()

    # Update DTC Data
    DTC_List = Get_DTC_Sts()
    config_Update_DTC_data(DTC_List)
    print("End Application")
    print("Number of readings now :",len(Room_temprate))
    print("DTC now :",DTC_List)
    time.sleep(30)
    return






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
    Set_Today()
    # create Startup Sheet
    Local_Excel_File = str(date.today())+ '.xlsx'
    Create_Excel_File(("Data/"+Local_Excel_File))
    Excel_Sheet["Sheet_Name"]=("Data/"+Local_Excel_File)
    Get_Config_Data()
    #Init Dtc From Config
    List = read_DTC_Config()
    Init_Update_DTC_Config_Sts(List)
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
    total_Tamp_Correct_Values = 0
    False1,False2,Ammonia = Sensor_Board_Handler_Runnable("Ammonia")
    Ammonia_Readings , Amonia_Num = Get_Valid_Readings(Ammonia)
    values = Ammonia_Readings.values()
    total_Ammonia = sum(values)
    if Amonia_Num != 0:
        Ammonia_sts["Ammonia"] = round((total_Ammonia/Amonia_Num),2)

    False3,False4,Air_Quality =Sensor_Board_Handler_Runnable("AIR")
    Air_Readings , Air_Num = Get_Valid_Readings(Air_Quality)
    values = Air_Readings.values()
    total_Air_Quality = sum(values)
    if Air_Num != 0:
        Air_sts["AirQuality"]=round((total_Air_Quality/Air_Num),2)
    Update_Air_Status(Air_sts["AirQuality"])

    Temprature , Humidity ,DataFalse = Sensor_Board_Handler_Runnable("Normal")
    Temp_Readings , Temp_Num = Get_Valid_Readings(Temprature)
    Humid_Readings, Humid_Num = Get_Valid_Readings(Humidity)

    '''
    This part when maximum 5 sensors avalaiable 
    Tamp_Correct_Values = Correct_factor_runable(Temprature,2)
    values = Tamp_Correct_Values.values()
    total_Tamp_Correct_Values = sum(values)
    Room_temp_sts["Room_temp"] = (total_Tamp_Correct_Values / len(Tamp_Correct_Values))
    '''
    values = Temp_Readings.values()
    total_Tamp_Correct_Values = sum(values)
    if Temp_Num != 0:
        Room_temp_sts["Room_temp"] = round((total_Tamp_Correct_Values/Temp_Num),2)
    values = Humid_Readings.values()
    total_Humidity = sum(values)
    if Humid_Num != 0:
        Room_Humid_sts["Room_Humid"]= round((total_Humidity/Humid_Num),2)
    Temprate1=float(Room_temp_sts["Room_temp"])
    Humidity1= float(Room_Humid_sts["Room_Humid"])
    print("Tamp ===========",Temprature)
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
    Set_Today()
    flag = Update_Day()
    if flag:
        Local_Excel_File = str(date.today()) + '.xlsx'
        Data["Date"] = str(date.today())
        Create_Excel_File(("Data/" + Local_Excel_File))
        Excel_Sheet["Sheet_Name"] = ("Data/" + Local_Excel_File)
    try:
        Write_to_Excel_data(Excel_data_frame,Excel_Sheet["Sheet_Name"])
    except:
        Excel_DIAG_Update("DTC_26")

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
        Internet_DIAG_Update("DTC_32")
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


def Get_Valid_Readings(Reading):
    delited_Key = []
    y = len(Reading)
    for key in Reading:
        if Reading[key] == 0:
            delited_Key.append(key)
    x = len(delited_Key)
    for i in range(x):
        del Reading[delited_Key[i]]

    valid_Reading_Nubmer = y - x
    return (Reading, valid_Reading_Nubmer)

def Collect_Config_Data():
    Config_List=[]
    Config_List.append(Data["Name"])
    Config_List.append(Data["Date"])
    Config_List.append(Data["Age"])
    Config_List.append(Data["Head_Cnt"])
    Config_List.append(Data["Temp_UP"])
    Config_List.append(Data["Temp_LW"])
    Config_List.append(Data["Ammonia_L"])
    return(Config_List)



def Update_Config_Data():
    Data["Head_Cnt"]=str(Head_count_sts["Room_head_count"])
    Data["Temp_UP"]=str(Limits["Temp_Up_limit"])
    Data["Temp_LW"]=str(Limits["Temp_Lw_limit"])
    Data["Ammonia_L"]=str(Limits["Ammonia"])
    List=Collect_Config_Data()
    config_Update_data(List)


def Get_Config_Data():
    List=read_Data_Config()
    Data["Name"] =List[0]
    Data["Date"]=List[1]
    Data["Age"]=List[2]
    Data["Head_Cnt"]=List[3]
    Data["Temp_UP"]=List[4]
    Data["Temp_LW"]=List[5]
    Data["Ammonia_L"]=List[6]
    Head_count_sts["Room_head_count"]=float(Data["Head_Cnt"])
    Limits["Temp_Up_limit"]=float(Data["Temp_UP"])
    Limits["Temp_Lw_limit"]=float(Data["Temp_LW"])
    Limits["Ammonia"]=float(Data["Ammonia_L"])