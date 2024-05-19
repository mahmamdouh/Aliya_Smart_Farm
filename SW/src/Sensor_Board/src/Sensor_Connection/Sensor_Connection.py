
import paho.mqtt.client as mqtt
import time

Message ={
 "Messaage":0,   
}
Sensor ={
 "Sensor":0, 
 "Message":0, 
}

def Get_Sensor_Data(SensorNUM,MessageNum):
	Rtn_Flg = 0
    Sensor["Sensor"] = SensorNUM
	Sensor["Message"] = MessageNum
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    mqtt_client.connect('localhost', 1883, 60) 
    # Connect to the MQTT server and process messages in a background thread. 
    mqtt_client.loop_start()
    time.sleep(5)
    mqtt_client.loop_stop()
    #print("outing")
	if Message["Messaage"] != 0 :
		Rtn_Flg = 1
	else:
		Rtn_Flg = 0
		
    return Message["Messaage"]




def on_connect(client, userdata, flags, rc):
    #print("Connected with result code "+str(rc))
    

    if Sensor["Sensor"] == 1 :
		if Sensor["Message"] == 1:
			client.subscribe("/Sensor1/DHT11_Temp")
		if Sensor["Message"] == 2:
			client.subscribe("/Sensor1/DHT11_Humid")
		if Sensor["Message"] == 3:
			client.subscribe("/Sensor1/AM2320_Temp")
		if Sensor["Message"] == 4:
			client.subscribe("/Sensor1/AM2320_Humid") 
		if Sensor["Message"] == 5:
			client.subscribe("/Sensor1/MQ135")
		if Sensor["Message"] == 6:
			client.subscribe("/Sensor1/DHT11_2_Temp")
		if Sensor["Message"] == 7:
			client.subscribe("/Sensor1/DHT11_2_Humid")
	
    elif Sensor["Sensor"] == 2:
        if Sensor["Message"] == 1:
			client.subscribe("/Sensor2/DHT11_Temp")
		if Sensor["Message"] == 2:
			client.subscribe("/Sensor2/DHT11_Humid")
		if Sensor["Message"] == 3:
			client.subscribe("/Sensor2/AM2320_Temp")
		if Sensor["Message"] == 4:
			client.subscribe("/Sensor2/AM2320_Humid") 
		if Sensor["Message"] == 5:
			client.subscribe("/Sensor2/MQ135")
		if Sensor["Message"] == 6:
			client.subscribe("/Sensor2/DHT11_2_Temp")
		if Sensor["Message"] == 7:
			client.subscribe("/Sensor2/DHT11_2_Humid")
    elif Sensor["Sensor"] == 3:
        if Sensor["Message"] == 1:
			client.subscribe("/Sensor3/DHT11_Temp")
		if Sensor["Message"] == 2:
			client.subscribe("/Sensor3/DHT11_Humid")
		if Sensor["Message"] == 3:
			client.subscribe("/Sensor3/AM2320_Temp")
		if Sensor["Message"] == 4:
			client.subscribe("/Sensor3/AM2320_Humid") 
		if Sensor["Message"] == 5:
			client.subscribe("/Sensor3/MQ135")
		if Sensor["Message"] == 6:
			client.subscribe("/Sensor3/DHT11_2_Temp")
		if Sensor["Message"] == 7:
			client.subscribe("/Sensor3/DHT11_2_Humid")
    elif Sensor["Sensor"] == 4:
         if Sensor["Message"] == 1:
			client.subscribe("/Sensor4/DHT11_Temp")
		if Sensor["Message"] == 2:
			client.subscribe("/Sensor4/DHT11_Humid")
		if Sensor["Message"] == 3:
			client.subscribe("/Sensor4/AM2320_Temp")
		if Sensor["Message"] == 4:
			client.subscribe("/Sensor4/AM2320_Humid") 
		if Sensor["Message"] == 5:
			client.subscribe("/Sensor4/MQ135")
		if Sensor["Message"] == 6:
			client.subscribe("/Sensor4/DHT11_2_Temp")
		if Sensor["Message"] == 7:
			client.subscribe("/Sensor4/DHT11_2_Humid")
    elif Sensor["Sensor"] == 5:
        if Sensor["Message"] == 1:
			client.subscribe("/Sensor5/DHT11_Temp")
		if Sensor["Message"] == 2:
			client.subscribe("/Sensor5/DHT11_Humid")
		if Sensor["Message"] == 3:
			client.subscribe("/Sensor5/AM2320_Temp")
		if Sensor["Message"] == 4:
			client.subscribe("/Sensor5/AM2320_Humid") 
		if Sensor["Message"] == 5:
			client.subscribe("/Sensor5/MQ135")
		if Sensor["Message"] == 6:
			client.subscribe("/Sensor5/DHT11_2_Temp")
		if Sensor["Message"] == 7:
			client.subscribe("/Sensor5/DHT11_2_Humid")
    elif Sensor["Sensor"] == 6:
        if Sensor["Message"] == 1:
			client.subscribe("/Sensor6/DHT11_Temp")
		if Sensor["Message"] == 2:
			client.subscribe("/Sensor6/DHT11_Humid")
		if Sensor["Message"] == 3:
			client.subscribe("/Sensor6/AM2320_Temp")
		if Sensor["Message"] == 4:
			client.subscribe("/Sensor6/AM2320_Humid") 
		if Sensor["Message"] == 5:
			client.subscribe("/Sensor6/MQ137")
		if Sensor["Message"] == 6:
			client.subscribe("/Sensor6/DHT11_2_Temp")
		if Sensor["Message"] == 7:
			client.subscribe("/Sensor6/DHT11_2_Humid")

        

    

def on_message(client, userdata, message):
    #print("Received message '" + str(message.payload) + "' on topic '" + message.topic)
    Message["Messaage"] = str(message.payload)
    #client.loop_stop()