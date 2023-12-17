/*
  Example for MCP3008 - Library for communicating with MCP3008 Analog to digital converter.
  Created by Uros Petrevski, Nodesign.net 2013
  Released into the public domain.
*/

#include "MCP3008.h"


// define pin connections
#define CS_PIN 15
#define CLOCK_PIN 14
#define MOSI_PIN 13
#define MISO_PIN 12

// put pins inside MCP3008 constructor
MCP3008 adc(CLOCK_PIN, MOSI_PIN, MISO_PIN, CS_PIN);

void setup() {
 
 // open serial port
 Serial.begin(9600);
  
}


void loop() {
  
  
  int val = adc.readADC(0); // read Chanel 0 from MCP3008 ADC
  Serial.println("Chanel 0");
  Serial.println(val);
  int val2 = adc.readADC(1); // read Chanel 0 from MCP3008 ADC
  Serial.println("Chanel 1");
  Serial.println(val2);
  
  
  // iterate thru all channels
  /*
  for (int i=0; i<8; i++) {
   int val = adc.readADC(i);
   Serial.print(val);
   Serial.print("\t");
   }
   Serial.println("");
  */
  
}
/*
  Example for MCP3008 - Library for communicating with MCP3008 Analog to digital converter.
  Created by Uros Petrevski, Nodesign.net 2013
  Released into the public domain.
*/
