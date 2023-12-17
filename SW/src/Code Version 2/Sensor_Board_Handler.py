import paho.mqtt.client as mqtt
from Sensor_Connection import Get_Sensor_Data
import re
from random import random
from itertools import combinations
from DTC import *
from Check_Connectivity import Check_Connection_Runnable
Temp_Data = {
    "Sensor1": 0,
    "Sensor2": 0,
    "Sensor3": 0,
    "Sensor4": 0,
    "Sensor5": 0,
    "Sensor6": 0,
}
Humid_Data = {
    "Sensor1": 0,
    "Sensor2": 0,
    "Sensor3": 0,
    "Sensor4": 0,
    "Sensor5": 0,
    "Sensor6": 0,
}
Air_Quality = {
    "Sensor1": 0,
    "Sensor2": 0,
    "Sensor3": 0,
    "Sensor4": 0,
    "Sensor5": 0,
    "Sensor6": 0,
}
Ammonia_Reading = {
    "Sensor1": 0,
    "Sensor2": 0,
    "Sensor3": 0,
    "Sensor4": 0,
    "Sensor5": 0,
    "Sensor6": 0,
}
Flags = {
    "DHT_1_T": 0,
    "DHT_1_H": 0,
    "DHT_2_T": 0,
    "DHT_2_H": 0,
    "Am2320_T": 0,
    "Am2320_H": 0,
    "MQ": 0,
}


def Sensor_Board_Handler(i, Type):
    Temp_Vald_Num = 0
    Humid_Vald_Num = 0
    DHT_1_T =0
    DHT_2_T =0
    Am2320_T=0
    DHT_1_H=0
    DHT_2_H=0
    Am2320_H=0
    #print("Request sensor",i, Type)
    if Type == "Normal":
        # print("DHT 11 Temp ===========================")
        message, Flags["DHT_1_T"] = Get_Sensor_Data(i, 1)
        if Flags["DHT_1_T"]:
            Flag = re.search("\d+\.\d+", message)
            if Flag:
                message1 = re.findall("\d+\.\d+", message)
                DHT_1_T = float(message1[0])
                Temp_Vald_Num = Temp_Vald_Num + 1
        else:
            DTC_section_selection(i,"DHT_1")
        # print("DHT 11 humid ===========================")
        message, Flags["DHT_1_H"] = Get_Sensor_Data(i, 2)
        if Flags["DHT_1_H"]:
            Flag = re.search("\d+\.\d+", message)
            if Flag:
                message1 = re.findall("\d+\.\d+", message)
                DHT_1_H = float(message1[0])
                Humid_Vald_Num = Humid_Vald_Num + 1
        else:
            DTC_section_selection(i,"DHT_1")
        # print("am  temp ===========================")
        message, Flags["Am2320_T"] = Get_Sensor_Data(i, 3)
        if Flags["Am2320_T"]:
            Flag = re.search("\d+\.\d+", message)
            if Flag:
                message1 = re.findall("\d+\.\d+", message)
                Am2320_T = float(message1[0])
                Temp_Vald_Num = Temp_Vald_Num + 1
        else:
            DTC_section_selection(i,"am2320")
        # print("am  humod ===========================")
        message, Flags["Am2320_H"] = Get_Sensor_Data(i, 4)
        if Flags["Am2320_H"]:
            Flag = re.search("\d+\.\d+", message)
            if Flag:
                message1 = re.findall("\d+\.\d+", message)
                Am2320_H = float(message1[0])
                Humid_Vald_Num = Humid_Vald_Num + 1
        else:
            DTC_section_selection(i,"am2320")
        # print("DHT 11 - 2 Temp ===========================")
        message, Flags["DHT_2_T"] = Get_Sensor_Data(i, 6)
        if Flags["DHT_2_T"]:
            Flag = re.search("\d+\.\d+", message)
            if Flag:
                message1 = re.findall("\d+\.\d+", message)
                DHT_2_T = float(message1[0])
                Temp_Vald_Num = Temp_Vald_Num + 1
        else:
            DTC_section_selection(i,"DHT_2")
        # print("DHT 11 - 2 humid ===========================")
        message, Flags["DHT_2_H"] = Get_Sensor_Data(i, 7)
        if Flags["DHT_2_H"]:
            Flag = re.search("\d+\.\d+", message)
            if Flag:
                message1 = re.findall("\d+\.\d+", message)
                DHT_2_H = float(message1[0])
                Humid_Vald_Num = Humid_Vald_Num + 1
        else:
            DTC_section_selection(i,"DHT_2")

        if Temp_Vald_Num == 0:
            Temp_Avarage = (DHT_1_T + DHT_2_T + Am2320_T) / 1
        else:
            Temp_Avarage = (DHT_1_T + DHT_2_T + Am2320_T) / Temp_Vald_Num
        if Humid_Vald_Num == 0:
            Humid_Avarage = (DHT_1_H + DHT_2_H + Am2320_H) / 1
        else:
            Humid_Avarage = (DHT_1_H + DHT_2_H + Am2320_H) / Humid_Vald_Num
        

        return Temp_Avarage, Humid_Avarage, 0

    elif Type == "AIR":
        #print("Request AIR ")
        # print("MQ135  ===========================")
        message, Flags["MQ"] = Get_Sensor_Data(i, 5)
        #print("ftech AIR",message, Flags["Ammon"])
        if Flags["MQ"]:
            Flag = re.search("\d+\.\d+", message)
            if Flag:
                message1 = re.findall("\d+\.\d+", message)
                AIR_q = float(message1[0])
                return 0, 0, AIR_q
            else:
                Select_Dtc_Number(i, "MQ")
                return 0,0,0
        else:
            return 0, 0, 0
    elif Type == "Ammonia":
        # print("MQ137  ===========================")
        message, Flags["MQ"] = Get_Sensor_Data(i, 5)
        if Flags["MQ"]:
            Flag = re.search("\d+\.\d+", message)
            if Flag:
                message1 = re.findall("\d+\.\d+", message)
                Ammonia = float(message1[0])
                return 0, 0, Ammonia
            else:
                Select_Dtc_Number(i, "MQ")
                return 0,0,0
        else:
            return 0, 0, 0
    else:
        return 0, 0, 0


def Sensor_Board_Handler_Runnable(Type):
    
    Temp_Data = {
        "Sensor1": 0,
        "Sensor2": 0,
        "Sensor3": 0,
        "Sensor4": 0,
        "Sensor5": 0,
        "Sensor6": 0,
    }
    Humid_Data = {
        "Sensor1": 0,
        "Sensor2": 0,
        "Sensor3": 0,
        "Sensor4": 0,
        "Sensor5": 0,
        "Sensor6": 0,
    }
    Air_Quality = {
        "Sensor1": 0,
        "Sensor2": 0,
        "Sensor3": 0,
        "Sensor4": 0,
        "Sensor5": 0,
        "Sensor6": 0,
    }
    Ammonia_Reading = {
        "Sensor1": 0,
        "Sensor2": 0,
        "Sensor3": 0,
        "Sensor4": 0,
        "Sensor5": 0,
        "Sensor6": 0,
    }
    Temp_Data_list = list(Temp_Data)
    Humid_Data_list = list(Humid_Data)
    Air_Quality_list = list(Air_Quality)
    Ammonia_Reading_List=list(Ammonia_Reading)
    for i in range(1,7):
        #Check_Connection_Runnable(i)
        #print("Index",i)
        Temp_Avarage, Humid_Avarage, Air_Quality1 = Sensor_Board_Handler(i, Type)
        index = i - 1       
        if Type =="AIR":
            Air_Quality[Air_Quality_list[index]] = Air_Quality1
        elif Type =="Ammonia":
            Ammonia_Reading[Ammonia_Reading_List[index]] = Air_Quality1
        elif Type == "Normal":
            Temp_Data[Temp_Data_list[index]] = Temp_Avarage
            Humid_Data[Humid_Data_list[index]] = Humid_Avarage
            
    if Type =="AIR":
        return Temp_Data, Humid_Data, Air_Quality
    elif Type =="Ammonia":
        return Temp_Data, Humid_Data, Ammonia_Reading
    elif Type =="Normal":        
        return Temp_Data, Humid_Data, Air_Quality



def DTC_section_selection(Sensor,Prefix):
    #select DTC number
    DTC=Select_Dtc_Number(Sensor,Prefix)
    if Sensor == 1:
        Sensor_Board_1_DIAG_Update(DTC)
    elif Sensor == 2:
        Sensor_Board_2_DIAG_Update(DTC)
    elif Sensor == 3:
        Sensor_Board_3_DIAG_Update(DTC)
    elif Sensor == 4:
        Sensor_Board_4_DIAG_Update(DTC)
    elif Sensor == 5:
        Sensor_Board_5_DIAG_Update(DTC)
    elif Sensor == 6:
        Sensor_Board_6_DIAG_Update(DTC)


#Comment
#DTC Type and mapping
# DHT_1
# DHT_2
# am2320
# MQ

def Select_Dtc_Number(Sensor,DTC):
    if DTC == "DHT_1":
        if Sensor == 1:
            return "DTC_2"
        elif Sensor == 2:
            return "DTC_6"
        elif Sensor == 3:
            return "DTC_10"
        elif Sensor == 4:
            return "DTC_14"
        elif Sensor == 5:
            return "DTC_18"
        elif Sensor == 6:
            return "DTC_22"
    elif DTC == "DHT_2":
        if Sensor == 1:
            return "DTC_2_2"
        elif Sensor == 2:
            return "DTC_6_2"
        elif Sensor == 3:
            return "DTC_10_2"
        elif Sensor == 4:
            return "DTC_14_2"
        elif Sensor == 5:
            return "DTC_18_2"
        elif Sensor == 6:
            return "DTC_22_2"
    elif DTC == "am2320":
        if Sensor == 1:
            return "DTC_3"
        elif Sensor == 2:
            return "DTC_7"
        elif Sensor == 3:
            return "DTC_11"
        elif Sensor == 4:
            return "DTC_15"
        elif Sensor == 5:
            return "DTC_19"
        elif Sensor == 6:
            return "DTC_23"
    elif DTC == "MQ":
        if Sensor == 1:
            return "DTC_4"
        elif Sensor == 2:
            return "DTC_8"
        elif Sensor == 3:
            return "DTC_12"
        elif Sensor == 4:
            return "DTC_16"
        elif Sensor == 5:
            return "DTC_20"
        elif Sensor == 6:
            return "DTC_24"


'''
TempFalse,HumidFalse,Ammonia = Sensor_Board_Handler_Runnable("Ammonia")
print("Ammonia output ",Ammonia)
TempFalse,HumidFalse,Air_Quality =Sensor_Board_Handler_Runnable("AIR")
print("Air output ",Air_Quality)
Temprature , Humidity ,DataFalse = Sensor_Board_Handler_Runnable("Normal")
print("Temp output ",Temprature , Humidity)



#Temprature , Humidity ,DataFalse = Sensor_Board_Handler_Runnable("Normal")
Sensor_Num = 6
print("Testing Sensor ============================ 6")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")

print("Sensor Data",Temprature , Humidity ,DataFalse)
DTC_n=Get_DTC_Sts()
print("DTC Now",DTC_n)

Sensor_Num = 1
print("Testing Sensor ============================ 1")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")

print("Sensor Data",Temprature , Humidity ,DataFalse)
DTC_n=Get_DTC_Sts()
print("DTC Now",DTC_n)

Sensor_Num = 3
print("Testing Sensor ============================ 3")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")

print("Sensor Data",Temprature , Humidity ,DataFalse)
DTC_n=Get_DTC_Sts()
print("DTC Now",DTC_n)

Sensor_Num = 2
print("Testing Sensor ============================ 2")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")
Temprature , Humidity ,DataFalse = Sensor_Board_Handler(Sensor_Num,"Normal")

print("Sensor Data",Temprature , Humidity ,DataFalse)
DTC_n=Get_DTC_Sts()
print("DTC Now",DTC_n)
'''