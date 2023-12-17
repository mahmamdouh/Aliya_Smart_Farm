


import paho.mqtt.client as mqtt
import time
Message ={
 "Messaage":0,   
}
Sensor ={
 "Sensor":0,   
}

def Get_Sensor_Data(SensorNUM):
    Sensor["Sensor"] = SensorNUM
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    mqtt_client.connect('localhost', 1883, 60) 
    # Connect to the MQTT server and process messages in a background thread. 
    mqtt_client.loop_start()
    time.sleep(20)
    mqtt_client.loop_stop()
    print("outing")
    return Message["Messaage"]




def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    
    # Connect to Sensor 1 ( PT100 - DHT )
    #sensor5 data stream (DHT_TEMP,DHT_Humid,PT100)
    if Sensor["Sensor"] == 1 :
        client.subscribe("/esp2/temperature22")
        client.subscribe("/esp2/temperature22")
    # Connect to Sensor 2 ( PT100 - DHT )
    #sensor5 data stream (DHT_TEMP,DHT_Humid,PT100)
    elif Sensor["Sensor"] == 2:
        client.subscribe("/Sensor2/Data_2")
        client.subscribe("/Sensor2/DTC_2")
    # Connect to Sensor 3 ( PT100 - DHT )
    #sensor5 data stream (DHT_TEMP,DHT_Humid,PT100)
    elif Sensor["Sensor"] == 3:
        client.subscribe("/Sensor3/Data_3")
        client.subscribe("/Sensor3/DTC_3")
    # Connect to Sensor 4 ( PT100 - DHT - MQ135 )
    #sensor5 data stream (DHT_TEMP,DHT_Humid,PT100,MQ)
    elif Sensor["Sensor"] == 4:
        client.subscribe("/Sensor4/Data_4")
        client.subscribe("/Sensor4/DTC_4")
    # Connect to Sensor 5 ( PT100 - DHT - MQ135 )
    #sensor5 data stream (DHT_TEMP,DHT_Humid,PT100,MQ)
    elif Sensor["Sensor"] == 5:
        client.subscribe("/Sensor5/Data_5")
        client.subscribe("/Sensor5/DTC_5")
    # Connect to Sensor 6 ( PT100 - DHT - MQ137 )
    #sensor6 data stream (DHT_TEMP,DHT_Humid,PT100,MQ)
    elif Sensor["Sensor"] == 6:
        client.subscribe("/Sensor5/Data_6")
        client.subscribe("/Sensor6/DTC_6")

    

def on_message(client, userdata, message):
    #print("Received message '" + str(message.payload) + "' on topic '" + message.topic)
    Message["Messaage"] = str(message.payload)
    #client.loop_stop()