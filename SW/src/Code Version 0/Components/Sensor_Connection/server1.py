import paho.mqtt.client as mqtt
from Sensor_Connection import Get_Sensor_Data

def main():
    while True:
        
        print("sensor 1")
        message=Get_Sensor_Data(1)

        print("DHT Temp")
        print(message)
        '''
        message=Get_Sensor_Data(2)
        message2 = message.replace("b' ","")
        message3 = message2.replace("'","")
        print("DHT HUMID")
        print(message3)
        
        message=Get_Sensor_Data(3)
        message2 = message.replace("b' ","")
        message3 = message2.replace("'","")
        print("GAS PPM")
        print(message3)

        print("sensor 2")
        message=Get_Sensor_Data(4)        
        message2 = message.replace("b' ","")
        message3 = message2.replace("'","")
        print(message3)
        #Get_Sensor_Data(2)
'''


main()

