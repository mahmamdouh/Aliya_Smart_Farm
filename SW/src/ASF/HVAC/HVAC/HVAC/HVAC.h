// HVAC.h : Include file for standard system include files,
// or project specific include files.

#pragma once

#include <iostream>
#include <vector>
#include <string>

using std::vector;
using std::string;

class Temprature
{
private: 
	double IndoorCurrentTemprature;
	double OutdoorCurrentTemprature;
	double Get_Indoor_Temprature();
	double Get_Outdoor_Temprature();
	double Temp_equilizer(double temp);
public :
	Temprature();
	double Get_current_Temp();
};
// TODO: Reference additional headers your program requires here.

class HVAC
{
private:
	vector <string> Heating_devices;
	vector <string> Cooling_devices;
	vector <string> Heating_devices_sts;
	vector <string> Cooling_devices_sts;
	bool Set_Heating_ON(string device);
	bool Set_Heating_OFF(string device);
	bool Set_Colling_ON(string device);
	bool Set_Colling_OFF(string device);
public:
	HVAC();
	string Get_HVAC_sts();
	void HVAC_Task();

};