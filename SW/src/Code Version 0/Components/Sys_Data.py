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
	"Head Cnt" : "500",
	"Temp_UP" : "30",
	"Temp_LW" : "25",
	"Air_UP" : "30",
	"Air_LW" : "2",
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
  "Air": 40,
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
  "AirQuality": 0
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
                   'temp': []})

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
  "Num_Of_Days": "",
}
###########################


#######################################################################################
############################ Standared Functions     ##################################
#######################################################################################



Room_temp =[]
time_stamp =[]
min_Temp_limit_stamp =[]
max_Temp_limit_stamp =[]



def Get_Date ():
    today_date = datetime.now()
    hournw =int(today_date.hour)
    miunw  =int(today_date.minute)
    miunwsub=miunw/100
    time=hournw+miunwsub
    return (time)
    
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
        Day_hour["Num_Of_Days"] = Day_hour["Num_Of_Days"] + 1
        return 1
    else:
        return 0