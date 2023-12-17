from Conf_IP import config_Update_data ,read_Data_Config
import sys
import os
import re
from DTC import *

def Ping_IP_CHeck(IP,Sens_Num):
    IP_Adress=IP+" -c2"
    print("Ping IP:",IP_Adress)
    for i in range(5):
        state = os.system("ping "+IP_Adress)
        print("Message",str(state))
        regi_Flag = re.search("0", str(state))
        if regi_Flag :
            print("Connected")
            break
        else:
            print("Not connected")
            DTC_Update_Connection(Sens_Num)
            break
        #print("Program:Status:============",state)
        
def DTC_Update_Connection(Sensor):
    #print("Sensor To set DTC :",Sensor)
    if Sensor == 1:
        Sensor_Board_1_DIAG_Update("DTC_1")
    elif Sensor == 2:
        Sensor_Board_2_DIAG_Update("DTC_5")
    elif Sensor == 3:
        Sensor_Board_3_DIAG_Update("DTC_9")
    elif Sensor == 4:
        #print("Set DTC 13")
        Sensor_Board_4_DIAG_Update("DTC_13")
    elif Sensor == 5:
        Sensor_Board_5_DIAG_Update("DTC_17")
    elif Sensor == 6:
        Sensor_Board_6_DIAG_Update("DTC_21")
        
def Check_Connection_Runnable(Sensor):
    IP_List= read_Data_Config()
    Ping_IP_CHeck(IP_List[Sensoe-1],Sensor)
    
Check_Connection_Runnable(1)