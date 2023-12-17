
///////////////////////////////////////////////////////////////
void loop() {
const int MQ137_PIN = A3;
const float RL_MQ137 = 1.0; // kohm (FC-22 module = 1.0 kohm)
const float CLEAN_AIR_RATIO_MQ137 = 3.6; // Taken from datasheet graph
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
sensorValue_MQ137 = analogRead(A3);
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



