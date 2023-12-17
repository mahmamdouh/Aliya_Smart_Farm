import time
import datetime
from datetime import datetime
import pandas as pd
#data file for global data

#######################################################################################
################################   Config Data       ##################################
#######################################################################################

Data ={
	"Name" : "Aliya",
	"Date" : "15/11",
    "Age" : "10",
	"Head_Cnt" : "500",
	"Temp_UP" : "30",
	"Temp_LW" : "25",
	"Ammonia_L" : "30",
    "Updte_Flag" : "30",
	}
#######################################################################################
################################ Alarm Status    ##################################
#######################################################################################
Alarm = {
  "Staus": False,
}
#######################################################################################
################################ HVAC Global Data    ##################################
#######################################################################################
HVAC_Active_Time = {
  "Active_High": False,
  "Active_Low": False,
}
HVAC_sys_sts = {
  "Heater_1_sts": False,
  "Heater_2_sts": False,
  "Heater_3_sts": False,
  "cooler_1_sts": False,
  "cooler_2_sts": False,
  "cooler_3_sts": False,

}

Limits = {
  "Temp_Lw_limit": 25,
  "Temp_Up_limit": 30,
  "Humid_Lw_limit": 10,
  "Humid_Up_limit": 40,
  "Ammonia": 10,
  "Air": 100,
}

HVAC_STM = {
  "State": "SB",
  "Previous_state": "SB",
}
# States
#1- SB
#2- Coling
#3- Coling_wait
#2- Warming
#3- Warming_wait
#######################################################################################
################## Internet Connection and server    ##################################
#######################################################################################

sys_status ={
    "internet_connection": "Disconected",
    "application": "not runing"
    
}
#######################################################################################
############################## Air Quality  Data    ##################################
#######################################################################################
Air_Quality_STM = {
  "State": "SB",
  "Previous_state": "SB",
}
# States
#1- SB
#2- Waiting
#3- Open_Air
#######################################################################################
############################## Sensor Boards Data    ##################################
#######################################################################################

Room_temp_sts = {
  "Room_temp": 0
}

Room_Humid_sts = {
  "Room_Humid": 0
}

Ammonia_sts = {
  "Ammonia": 0
}

Air_sts = {
  "AirQuality": 0,
  "Condition": "Good",
}

#######################################################################################
############################ Room production Data    ##################################
#######################################################################################

Head_count_sts = {
  "Room_head_count": 50,
  "Age": 0,
}

Operator_HVAC_sys_sts = {
  "Food": 0,
  "Death": 0,
  "Operator_name": "None",
  "Operator_notic": "None",
}


#######################################################################################
############################ Excel Data _ Data    ##################################
#######################################################################################

Excel_data_frame = pd.DataFrame({'time': [],
                   'temp': [],'Humid': [],'Ammonia': [],'Air': [],'HVAC-STM': [],'Air-STM': []})

worksheet = {
  "worksheet": None,

}

Excel_Sheet = {
  "Sheet_Name": "None",

}
#######################################################################################
############################ Time control _ Data    ##################################
#######################################################################################


previous = {
  "previous_flag": 0,
  "previous_temp": 0,
}

Window_2_status = {
  "Window_open": 0,
  "Data_save": 0,
  "Window_closed": 0,
}






Day_hour = {
  "Today" : 0,
  "Last_Day": 0,
  "Num_Of_Days": 0,
}
###########################


#######################################################################################
############################ Standared Functions     ##################################
#######################################################################################







def Get_Date ():
    today_date = datetime.now()
    hournw =int(today_date.hour)
    miunw  =int(today_date.minute)
    miunwsub=miunw/100
    time=hournw+miunwsub
    rtn =round(time,2)
    return (rtn)


def time_to_sleep (time1):
    time.sleep(time1)


def Set_Today():
    localtime = time.localtime()
    day = int(localtime.tm_mday)
    Day_hour["Today"] = day


def Update_Day():
    localtime = time.localtime()
    day = int(localtime.tm_mday)
    if Day_hour["Today"] != Day_hour["Last_Day"]:
        Day_hour["Last_Day"] = Day_hour["Today"]
        Day_hour["Num_Of_Days"] = int(Day_hour["Num_Of_Days"]) + 1
        return 1
    else:
        return 0
    
    
  
Day_12_hour = {
  "AM_PM": "am",
  "Change_Flag": 0,
  "Previous_Day_time": "",
  "Current_Day_time": "" ,
}
def Update_12hur():
    Am_Pm = Day_12_hour["AM_PM"]
    localtime = time.localtime()
    Day_Night = time.strftime("%P",localtime)
    #print(Day_Night)
    Day_12_hour["AM_PM"] = str(Day_Night)
    if Am_Pm != Day_12_hour["AM_PM"] :
        Day_12_hour["Change_Flag"] = 1