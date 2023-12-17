import paho.mqtt.client as mqtt
from Sensor_Connection import Get_Sensor_Data

def main():
    message=Get_Sensor_Data(1)
    print("message 1")
    print(message)
    
    message=Get_Sensor_Data(2)
    print("message 2")
    print(message)
    #Get_Sensor_Data(2)



main()

