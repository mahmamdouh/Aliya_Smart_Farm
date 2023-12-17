import paho.mqtt.client as mqtt
from Sensor_Connection import Get_Sensor_Data
import re
from random import random
from itertools import combinations

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
Flags = {
    "DHT_1_T": 0,
    "DHT_1_H": 0,
    "DHT_2_T": 0,
    "DHT_2_H": 0,
    "Am2320_T": 0,
    "Am2320_H": 0,
    "Ammon": 0,
}


def Sensor_Board_Handler(i, Type):
    Temp_Vald_Num = 0
    Humid_Vald_Num = 0
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
            DTC_SB_DHT_1()
        # print("DHT 11 humid ===========================")
        message, Flags["DHT_1_H"] = Get_Sensor_Data(i, 2)
        if Flags["DHT_1_H"]:
            Flag = re.search("\d+\.\d+", message)
            if Flag:
                message1 = re.findall("\d+\.\d+", message)
                DHT_1_H = float(message1[0])
                Humid_Vald_Num = Humid_Vald_Num + 1
        # print("am  temp ===========================")
        message, Flags["Am2320_T"] = Get_Sensor_Data(i, 3)
        if Flags["Am2320_T"]:
            Flag = re.search("\d+\.\d+", message)
            if Flag:
                message1 = re.findall("\d+\.\d+", message)
                Am2320_T = float(message1[0])
                Temp_Vald_Num = Temp_Vald_Num + 1
        # print("am  humod ===========================")
        message, Flags["Am2320_H"] = Get_Sensor_Data(i, 4)
        if Flags["Am2320_H"]:
            Flag = re.search("\d+\.\d+", message)
            if Flag:
                message1 = re.findall("\d+\.\d+", message)
                Am2320_H = float(message1[0])
                Humid_Vald_Num = Humid_Vald_Num + 1
        # print("DHT 11 - 2 Temp ===========================")
        message, Flags["DHT_2_T"] = Get_Sensor_Data(i, 6)
        if Flags["DHT_2_T"]:
            Flag = re.search("\d+\.\d+", message)
            if Flag:
                message1 = re.findall("\d+\.\d+", message)
                DHT_2_T = float(message1[0])
                Temp_Vald_Num = Temp_Vald_Num + 1
        # print("DHT 11 - 2 humid ===========================")
        message, Flags["DHT_2_H"] = Get_Sensor_Data(i, 7)
        if Flags["DHT_2_H"]:
            Flag = re.search("\d+\.\d+", message)
            if Flag:
                message1 = re.findall("\d+\.\d+", message)
                DHT_2_H = float(message1[0])
                Humid_Vald_Num = Humid_Vald_Num + 1

        Temp_Avarage = (DHT_1_T + DHT_2_T + Am2320_T) / Temp_Vald_Num
        Humid_Avarage = (DHT_1_H + DHT_2_H + Am2320_H) / Humid_Vald_Num

        return (Temp_Avarage, Humid_Avarage, 0)

    if Type == "AIR" and ((i == 4) or (i == 5)):
        # print("MQ135  ===========================")
        message, Flags["Ammon"] = Get_Sensor_Data(i, 5)
        if Flags["Ammon"]:
            Flag = re.search("\d+\.\d+", message)
            if Flag:
                message1 = re.findall("\d+\.\d+", message)
                Ammon = float(message1[0])
        Air_Quality = Ammon
        return (0, 0, Air_Quality)
    elif Type == "Ammonia" and i == 6:
        # print("MQ137  ===========================")
        message, Flags["Ammon"] = Get_Sensor_Data(i, 5)
        if Flags["Ammon"]:
            Flag = re.search("\d+\.\d+", message)
            if Flag:
                message1 = re.findall("\d+\.\d+", message)
                Ammonia = float(message1[0])
        Ammonia = Ammonia
        return (0, 0, Ammonia)
    else:
        return (0, 0, 0)


def Sensor_Board_Handler_Runnable(SensorRange, Type):
    Temp_Data_list = list(Temp_Data)
    Humid_Data_list = list(Humid_Data)
    Air_Quality_list = list(Air_Quality)
    for i in range(SensorRange[0], SensorRange[1]):
        Temp_Avarage, Humid_Avarage, Air_Quality1 = Sensor_Board_Handler(i, Type)
        index = i - 1
        Temp_Data[Temp_Data_list[index]] = Temp_Avarage
        Humid_Data[Humid_Data_list[index]] = Humid_Avarage
        Air_Quality[Air_Quality_list[index]] = Air_Quality1
    return Temp_Data, Humid_Data, Air_Quality

'''
print("After ==================================")
print(Sensor_Board_Handler_Runnable([1, 7], "Ammonia"))
'''
