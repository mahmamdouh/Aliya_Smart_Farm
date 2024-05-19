// HVAC.h : Include file for standard system include files,
// or project specific include files.

#pragma once
#include <iostream>
#include <vector>
#include <string>



/**********************************************************************
********************** Global variables  ****************************** 
***********************************************************************/

using std::vector;
using std::string;

class Temprature
{
private: 
	double IndoorCurrentTemprature;
	double OutdoorCurrentTemprature;
	double Get_Indoor_Temprature();
	double Get_Outdoor_Temprature();
	double Temp_equilizer(vector <double> data);
public :
	Temprature();
	double Get_current_Temp(string Type);
};
// TODO: Reference additional headers your program requires here.

class HVAC
{
private:
	double Temp_Low_Limit;
	double Temp_High_Limit;
	vector <string> Heating_devices;
	vector <string> Cooling_devices;
	vector <string> Heating_devices_sts;
	vector <string> Cooling_devices_sts;
	string HVAC_ERR_Sts;
	double HVAC_waiting_Timer;
	// TODO Update this valur from Machine constants and set avaliable only for DIAG programming session.
	const double HVAC_Alarm_Limit = 5;
	string STM;
	bool Set_Heating_ON(string device);
	bool Set_Heating_OFF(string device);
	bool Set_Colling_ON(string device);
	bool Set_Colling_OFF(string device);
	string HVAC_STM(string state, double Temp);
public:
	HVAC();
	string Get_HVAC_sts();
	void HVAC_Task();
	bool HVAC_Set_Temp_limits(double High, double Low);

};