import time
import datetime
from datetime import datetime
import pandas as pd
#data file for global data
HVAC_sys_sts = {
  "Heater_1_sts": False,
  "Heater_2_sts": False,
  "Heater_3_sts": False,
  "cooler_1_sts": False,
  "cooler_2_sts": False,
  "cooler_3_sts": False,

}

Room_temp_sts = {
  "Room_temp": 0
}

Ammonia_sts = {
  "Ammonia": 0
}

Head_count_sts = {
  "Room_head_count": 50
}

previous = {
  "previous_flag": 0,
  "previous_temp": 0,
}

Window_2_status = {
  "Window_open": 0,
  "Data_save": 0,
  "Window_closed": 0,
}

worksheet = {
  "worksheet": None

}


Operator_HVAC_sys_sts = {
  "Food": 0,
  "Death": 0,
  "Operator_name": "None",
  "Operator_notic": "None",


}

Day_12_hour = {
  "AM_PM": "am",
  "Change_Flag": 0,
}
###############################
# data frame for local Excel
Excel_data_frame = pd.DataFrame({'time': [],
                   'temp': []})


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
    
def Update_12hur():
    Am_Pm = Day_12_hour["AM_PM"]
    localtime = time.localtime()
    Day_Night = time.strftime("%P",localtime)
    print(Day_Night)
    Day_12_hour["AM_PM"] = str(Day_Night)
    if Am_Pm != Day_12_hour["AM_PM"] :
        Day_12_hour["Change_Flag"] = 1