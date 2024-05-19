// Liberary Include

#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include "DHT.h"
#include <Wire.h>
#include "AM2320.h"
#include "MQ135.h"

//Global # Defines 
//##################################################################
//####               Define Local variable                      ####
//##################################################################
#define Client_ID               "Sensor_1"

#define Temprature_data_DHT	    "/Sensor1/DHT_temperature"
#define Humidity_data_DHT	    "/Sensor1/DHT_humidity"
#define Temprature_data_Pt100	"/Sensor1/PT100_temperature"
#define Airquality_data         "/Sensor1/MQ135_Air"
#define Ammonia_data	        "/Sensor1/MQ137_Ammonia"

//DTC flags
#define DHT_DTC_F	    "/Sensor1/DHT_DTC"
#define PT100_DTC_F	    "/Sensor1/PT100_DTC"
#define MQ135_DTC_F	    "/Sensor1/MQ135_DTC"
#define MQ137_DTC_F	    "/Sensor1/MQ137_DTC"
// MQ135
#define MQ135_PIN A0

MQ135 mq135_sensor(MQ135_PIN);



//AM2320 Black
AM2320 th;

// DHT11
#define DHTTYPE DHT11   // DHT 22  (AM2302), AM2321

// DHT Sensor
const int DHTPin = 2;
const int DHTPin2 = 13;

// Initialize DHT sensor.
DHT dht(DHTPin, DHTTYPE);
DHT dht2(DHTPin2, DHTTYPE);

// Global Variable 
float temperature = 21.0; // Assume current temperature. Recommended to measure with DHT22
float humidity = 25.0; // Assume current humidity. Recommended to measure with DHT22

float DHT_1_temperature = 0; // Assume current temperature. Recommended to measure with DHT22
float DHT_1_humidity = 0; // Assume current humidity. Recommended to measure with DHT22

float DHT_2_temperature = 0; // Assume current temperature. Recommended to measure with DHT22
float DHT_2_humidity = 0; // Assume current humidity. Recommended to measure with DHT22

float AM2320_temperature = 0; // Assume current temperature. Recommended to measure with DHT22
float AM2320_humidity = 0; // Assume current humidity. Recommended to measure with DHT22

float MQ135_PPM = 0; // Assume current humidity. Recommended to measure with DHT22

//AM2320_DTC
int AM2320_CRC =0 ;
int AM2320_offLine =0 ;
// Mqtt connection Data
const char* ssid = "mahmoud2";
const char* password = "Likesome=1994";

// Change the variable to your Raspberry Pi IP address, so it connects to your MQTT broker
const char* mqtt_server = "192.168.0.10";

// Initializes the espClient
WiFiClient espClient;
PubSubClient client(espClient);



// Timers auxiliar variables
long now = millis();
long lastMeasure = 0;


/*
#######################################################################
# function name :    DHT11_1                                          #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
*/
int DHT11_2_Runnable()
{
  float h = dht2.readHumidity();
    // Read temperature as Celsius (the default)
    float t = dht2.readTemperature();
    // Read temperature as Fahrenheit (isFahrenheit = true)
    float f = dht2.readTemperature(true);
  DHT_2_temperature = t;
  DHT_2_humidity = h;
   
    // Check if any reads failed and exit early (to try again).
    if (isnan(h) || isnan(t) || isnan(f)) {
      Serial.println("Failed to read from DHT sensor!");
      return 0;
    }
  return 1;
}
/*
#######################################################################
# function name :    DHT11_1                                          #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
*/
int DHT11_1_Runnable()
{
	float h = dht.readHumidity();
    // Read temperature as Celsius (the default)
    float t = dht.readTemperature();
    // Read temperature as Fahrenheit (isFahrenheit = true)
    float f = dht.readTemperature(true);
	DHT_1_temperature = t;
	DHT_1_humidity = h;
   
    // Check if any reads failed and exit early (to try again).
    if (isnan(h) || isnan(t) || isnan(f)) {
      Serial.println("Failed to read from DHT sensor!");
      return 0;
    }
	return 1;
}
/*
#######################################################################
# function name :    AM2320                                           #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
*/
int AM2320_Runnable()
{
	int Rtn_Flg = 0;
	switch(th.Read()) {
    case 2:
      AM2320_CRC = 1 ;
	  Rtn_Flg =0;
      break;
    case 1:
      AM2320_offLine = 1 ;
	  Rtn_Flg =0;
      break;
    case 0:

	  AM2320_temperature = th.t;
      AM2320_humidity = th.h;
	  Rtn_Flg =1;
      break;
  } 
  return Rtn_Flg;
}
/*
#######################################################################
# function name :    MQ135_correctedPPM                               #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
*/
float MQ135_correctedPPM()
{
	float rzero = mq135_sensor.getRZero();
	float correctedRZero = mq135_sensor.getCorrectedRZero(temperature, humidity);
	float resistance = mq135_sensor.getResistance();
	float ppm = mq135_sensor.getPPM();
	float correctedPPM = mq135_sensor.getCorrectedPPM(temperature, humidity);
    
	
	
	// Publishes MQ data of air quality
	return 	correctedPPM;

}


/*
#######################################################################
# function name :    setup_wifi                                       #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
*/
void setup_wifi() {
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("WiFi connected - ESP IP address: ");
  Serial.println(WiFi.localIP());
}

/*
#######################################################################
# function name :    callback                                         #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
*/
void callback(String topic, byte* message, unsigned int length) {
  Serial.print("Message arrived on topic: ");
  Serial.print(topic);
  Serial.print(". Message: ");
  String messageTemp;
  
  for (int i = 0; i < length; i++) {
    Serial.print((char)message[i]);
    messageTemp += (char)message[i];
  }
  Serial.println();

  
  Serial.println();
}

/*
#######################################################################
# function name :    reconnect                                        #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
*/
void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    
    if (client.connect("Sensor1")) {
      Serial.println("connected");  
      client.subscribe("Sensor1/4");
      client.subscribe("Sensor1/5");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(15000);
    }
  }
}


/*
#######################################################################
# function name :    setup                                            #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
*/
void setup() {
  dht.begin();
  
  Serial.begin(9600);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

/*
#######################################################################
# function name :    main_Loop                                        #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
*/
void loop() {
  
  // Check connection
  if (!client.connected()) 
  {
    reconnect();
  }
  //check Client
  if(!client.loop())
	 client.connect("Sensor1");
 
 
  // Main Tasks 
  // Task : 1 " read DHT 11 data 
  if (DHT11_2_Runnable())
  {
    static char DHT11_2_Temp[7];
  dtostrf(DHT_1_temperature, 6, 2, DHT11_2_Temp);
  client.publish("/Sensor1/DHT11_2_Temp", DHT11_2_Temp);
  static char DHT11_2_Humid[7];
  dtostrf(DHT_1_humidity, 6, 2, DHT11_2_Humid);
  client.publish("/Sensor1/DHT11_2_Humid", DHT11_2_Humid);
  Serial.println("DHT11-2 ===================");
  Serial.println(DHT11_2_Temp);
  Serial.println(DHT11_2_Humid);
  }   
  // Task : 2 " read DHT 11 data 
  if (DHT11_1_Runnable())
  {
    static char DHT11_Temp[7];
	dtostrf(DHT_1_temperature, 6, 2, DHT11_Temp);
	client.publish("/Sensor1/DHT11_Temp", DHT11_Temp);
	static char DHT11_Humid[7];
	dtostrf(DHT_1_humidity, 6, 2, DHT11_Humid);
	client.publish("/Sensor1/DHT11_Humid", DHT11_Humid);
	Serial.println("DHT11 ===================");
	Serial.println(DHT11_Temp);
	Serial.println(DHT11_Humid);
  }	  
 
  // Task : 3 " read Am2320 data 
 if (AM2320_Runnable())
  {
    static char AM2320_Temp[7];
	dtostrf(AM2320_temperature, 6, 2, AM2320_Temp);
	client.publish("/Sensor1/AM2320_Temp", AM2320_Temp);
	static char AM2320_Humid[7];
	dtostrf(AM2320_humidity, 6, 2, AM2320_Humid);
	client.publish("/Sensor1/AM2320_Humid", AM2320_Humid);
	Serial.println("AM2320 ===================");
	Serial.println(AM2320_Temp);
	Serial.println(AM2320_Humid);
  }	 
  // Task : 4 " read Mq135 data 
  MQ135_PPM = MQ135_correctedPPM();
  static char Air_Quality[7];
  dtostrf(MQ135_PPM, 6, 2, Air_Quality);
  client.publish("/Sensor1/MQ135", Air_Quality);
  Serial.println("MQ135 ===================");
  Serial.println(Air_Quality);
  delay(300);
  
  
}
