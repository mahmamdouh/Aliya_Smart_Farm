/*
##################################################################
##																##
##		   /\		|		|	\		/		/\				##
##		  /	 \		|		|    \     /	   /  \			    ##
##		 /	  \		|		|	  \   /		  /	   \		    ##
##		/------\	|		|	   \ /	   	 /------\			##
##	   /	 	\	|_____	|	|___/		/		 \			##
## 																##
## 			    	Aliya Smart System							##
## 			         WWW.Aliya-Co.com							##
##################################################################
##################################################################
##  Project        : Aliya-Smart-Farm                           ##
##	component name : Read Correct Filter						##
##	Author         : Mahmoud Elmohtady							##
##	Date           : 31/10/2021									##
##																##
##																##
##################################################################
*/

//##################################################################
//####                  Liberary Include                        ####
//##################################################################
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include "DHT.h"
#define DHTTYPE DHT11   // DHT 22  (AM2302), AM2321
#include "MQ135.h"
#include <MCP3008.h>
 

//##################################################################
//####               Define Global variable                     ####
//##################################################################
//MCP 3008 Pin definitionsa
//define pin connections
#define CS_PIN D8 //15
#define CLOCK_PIN D5 //14
#define MOSI_PIN D7 //13
#define MISO_PIN D6 //12
 
#define MQ137_PIN 0
#define MQ135_PIN 1
#define PT100_PIN 2
 
// MQ 135 variable 

MQ135 mq135_sensor(MQ135_PIN);

float temperature = 21.0; // Assume current temperature. Recommended to measure with DHT22
float humidity = 25.0; // Assume current humidity. Recommended to measure with DHT22

// MQ 137 varabile 
const float RL_MQ137 = 1.0; // kohm (FC-22 module = 1.0 kohm)
const float CLEAN_AIR_RATIO_MQ137 = 3.6; // Taken from datasheet graph

// MQTT connection variablea
const char* ssid = "Network Name";
const char* password = "Network Password";

// Change the variable to your Raspberry Pi IP address, so it connects to your MQTT broker
const char* mqtt_server = "";

// Initializes the espClient
WiFiClient espClient;
PubSubClient client(espClient);

// DHT Sensor
const int DHTPin = 14;

// Initialize DHT sensor.
DHT dht(DHTPin, DHTTYPE);

// Timers auxiliar variables
long now = millis();
long lastMeasure = 0;

// DTC 
int DHT_DTC_cnt = 0;
int PT100_DTC_cnt = 0;
int MQ135_DTC_cnt = 0;
int MQ137_DTC_cnt = 0;

// PT100 variables 
// Define Variables
float V;
float temp;
float Rx;

// Variables to convert voltage to resistance
float C = 79.489;
float slope = 14.187;

// Variables to convert resistance to temp
float R0 = 100.0;
float alpha = 0.00385;

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

//##################################################################
//####                Function Definition                       ####
//##################################################################
// initialization
MCP3008 adc(CLOCK_PIN, MOSI_PIN, MISO_PIN, CS_PIN);
/*
#######################################################################
# function name :                                                     #
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
# function name :                                                     #
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
# function name :                                                     #
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
    
    if (client.connect(Client_ID)) {
      Serial.println("connected");  
      //client.subscribe("esp8266/4");
      //client.subscribe("esp8266/5");
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
# function name :                                                     #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
*/
float MQ137_Update()
{

float sensorValue_MQ137;
float sensor_volt_MQ137;
float Rs_MQ137; // kohm
const float R0_MQ137 = 16.10; // kohm , from the R0 finder sketch
float AirFraction_MQ137;
float AirFractionMin_MQ137 = 0.118851;
float AirFractionMax_MQ137 = 0.388153;
float AirFractionCurva33_MQ137;
float AirFractionCurva85_MQ137;
float AirFractionCalibr_MQ137;
//Calculating Rs from analog data
sensorValue_MQ137 = adc.readADC(MQ137_PIN);
sensor_volt_MQ137 = sensorValue_MQ137*(5.0/1023.0); //Convert to voltage
Rs_MQ137 = ((5.0*RL_MQ137)/sensor_volt_MQ137)-RL_MQ137; //Calculate Rs
AirFraction_MQ137 = Rs_MQ137/R0_MQ137;

float h1 = bme1.readHumidity()+6.89;
float t1 = bme1.readTemperature()+0.55;


float ppmNH3calibr;
float ppmNH3;
// Calibration of MQ137 considering Temperature and relative humidity based on Hanwen datasheet, using polinomial regression
AirFractionCurva33_MQ137 = 0.0003 * pow(t1, 2) - 0.0255 * t1 + 1.4004;
AirFractionCurva85_MQ137 = 0.0003 * pow(t1, 2) - 0.0231 * t1 + 1.2808;
if (h1 >= 0 && h1 < 59) {
AirFractionCalibr_MQ137 = AirFraction_MQ137 / AirFractionCurva33_MQ137;
}
else 
AirFractionCalibr_MQ137 = AirFraction_MQ137 / AirFractionCurva85_MQ137;
}
/// Convertion to ppm of NH3:
float expoente_MQ137 = 1 / (-0.257);
ppmNH3 = pow((AirFraction_MQ137 / 0.587), expoente_MQ137);
ppmNH3calibr = pow((AirFractionCalibr_MQ137 / 0.587), expoente_MQ137);
//round [NH3] to an int and then put the values of [NH3], RH and T in the respective arrays:
if (ppmNH3calibr == 0)
{MQ137_DTC_cnt++; }	
return ppmNH3calibr ; 
}
/*
#######################################################################
# function name :                                                     #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
*/
char DTC_CHECK(int counter)
{
	if (counter > 10)
	{
	  DHT_DTC_cnt = 0 ;
	  return '1' ;}
    else
	{ return '0';}
}

/*
#######################################################################
# function name :                                                     #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
*/
float Pt100_Update()
{
  // Bits to Voltage
  V = (adc.readADC(PT100_PIN)/1023.0)*5.0; // (bits/2^n-1)*Vmax 
  // Voltage to resistance
  Rx = V*slope+C; //y=mx+c
  // Resistance to Temperature
  temp= (Rx/R0-1.0)/alpha; // from Rx = R0(1+alpha*X)
  // Uncommect to convet celsius to fehrenheit
  // temp = temp*1.8+32; 
  return temp ;

}


/*
#######################################################################
# function name :                                                     #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
*/
void loop() {
  // connect to broker
  if (!client.connected()) {
    reconnect();
  }
  if(!client.loop())

    client.connect(Client_ID);
   
  // DHT Operations   
  now = millis();
  // Publishes new temperature and humidity every 10 seconds
  
  static char temperatureTemp[7];
  static char humidityTemp[7];
  if (now - lastMeasure > 10000) {
    lastMeasure = now;
	
    // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
    float h = dht.readHumidity();
    // Read temperature as Celsius (the default)
    float t = dht.readTemperature();
    // Read temperature as Fahrenheit (isFahrenheit = true)
    float f = dht.readTemperature(true);

    // Check if any reads failed and exit early (to try again).
    if (isnan(h) || isnan(t) || isnan(f)) {
      Serial.println("Failed to read from DHT sensor!");
      DHT_DTC_cnt++;	  
      return;
    }
	else
	{

    // Computes temperature values in Celsius
    //float hic = dht.computeHeatIndex(t, h, false);
    
    dtostrf(t, 6, 2, temperatureTemp);
    dtostrf(h, 6, 2, humidityTemp);
	
	Serial.print("Humidity: ");
    Serial.print(h);
    Serial.print("\t Temperature: ");
    Serial.print(t);
    Serial.print(" *C ");
    Serial.println("");
	}
    // Publishes Temperature and Humidity values

	//update temp and humid variable for calibrate MQ135
    temperature = float(t);
	humidity = float(h);
	
	/*
	// MQ135 data//////////////////////////////////////////////////////////////////////////////////
	///////////////////////////////////////////////////////////////////////////////////////////
	*/
	float rzero = mq135_sensor.getRZero();
	float correctedRZero = mq135_sensor.getCorrectedRZero(temperature, humidity);
	float resistance = mq135_sensor.getResistance();
	float ppm = mq135_sensor.getPPM();
	float correctedPPM = mq135_sensor.getCorrectedPPM(temperature, humidity);
    
	Serial.print("MQ135 RZero: ");
	Serial.print(rzero);
	Serial.print("\t MQ135 Corrected RZero: ");
	Serial.print(correctedRZero);
	Serial.print("\t MQ135 Resistance: ");
	Serial.print(resistance);
	Serial.print("\t MQ135 PPM: ");
	Serial.print(ppm);
	Serial.print("\t MQ135 Corrected PPM: ");
	Serial.print(correctedPPM);
	Serial.println("MQ135 ppm");
	
	// Publishes MQ data of air quality
	static char Airquality[7];
	dtostrf(correctedPPM, 6, 2, Airquality);
	
	
	// MQ137 read data 
	static char MQ137_Nh3[7];
	float MQ_NH3 = MQ137_Update();
	dtostrf(MQ_NH3, 6, 2, MQ137_Nh3);
	
	// PT100 temprature read 
	static char PT100_data[7];
	float PT100_Temp = Pt100_Update();
	dtostrf(PT100_Temp, 6, 2, PT100_data);
	// Update Data DTC
	char DHT_DTC = DTC_CHECK(DHT_DTC_cnt);
	char MQ137_DTC = DTC_CHECK(MQ137_DTC_cnt);
	
	// publish data

    client.publish(Temprature_data_DHT, temperatureTemp);
    client.publish(Humidity_data_DHT, humidityTemp);
	client.publish(Temprature_data_Pt100, PT100_data);
	client.publish(Airquality_data, Airquality);
	client.publish(Ammonia_data, MQ137_Nh3);
	
	
	client.publish(DHT_DTC_F, DHT_DTC);
	client.publish(MQ137_DTC_F, MQ137_DTC);
	client.publish(DHT_DTC_F, DHT_DTC);

//#define PT100_DTC_F	    "/Sensor1/PT100_DTC"
//#define MQ135_DTC_F	    "/Sensor1/MQ135_DTC"


     
  delay(300);

  }
}

