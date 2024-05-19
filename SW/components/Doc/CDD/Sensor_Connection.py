


import paho.mqtt.client as mqtt
import time
Message =""
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
    return Message




def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    #print("Sensor")
    #print(Sensor["Sensor"])
    # Subscribing in on_connect() means that if we lose the connection and
    if Sensor["Sensor"] == 1 :
        #print("sub")
        client.subscribe("/esp2/temperature")
    elif Sensor["Sensor"] == 2:
        client.subscribe("/esp8266/temperature")
    

def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '" + message.topic)
    Message = str(message.payload)
    #client.loop_stop()