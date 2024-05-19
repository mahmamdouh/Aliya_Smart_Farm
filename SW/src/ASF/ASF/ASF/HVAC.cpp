// HVAC.cpp : Defines the entry point for the application.
//

#include "HVAC.h"
#include "Sensor_H.h"
#include <iostream>
using std::vector;
using std::string;
using std::cout;
using std::endl;
using std::to_string;

using namespace std;


// Temprature class
Temprature::Temprature() : IndoorCurrentTemprature(20), OutdoorCurrentTemprature(20)
{

}

double Temprature::Get_Indoor_Temprature()
{
	// create object from sensor handler
	Temp_Sensor Temp_sensor;
	// vector local variable for temprature readings.
	vector <double> Temp;
	// Read temprature sensor number of times.
	Temp = Temp_sensor.SENSOR_H_get_temp(5, "Indoor");
	// request temprature equalization.
	double Temp_eq = Temp_equilizer(Temp);
	return Temp_eq;
}
double Temprature::Get_Outdoor_Temprature()
{
	// create object from sensor handler
	Temp_Sensor Temp_sensor;
	// vector local variable for temprature readings.
	vector <double> Temp;
	// Read temprature sensor number of times.
	Temp = Temp_sensor.SENSOR_H_get_temp(5, "Outdoor");
	// request temprature equalization.
	double Temp_eq = Temp_equilizer(Temp);
	return Temp_eq;
}
double Temprature::Temp_equilizer(vector <double> data)
{
	// TODO : implementation based on equilizer component.
	double temp1 = 0 ;
	for (auto temp : data)
	{
		cout << temp << endl;
		temp1 = temp;
	}
	return temp1;
}

double Temprature::Get_current_Temp(string Type)
{
	double Temp;
	if (Type == "Indoor")
	{
		Temp = Get_Indoor_Temprature();
	}
	else if (Type == "Outdoor")
	{
		Temp = Get_Indoor_Temprature();
	}
	else
	{
		// TODO : Report error
	}
	return Temp;
}


// HVAC class
HVAC::HVAC() : Heating_devices({"Heating_D1", "Heating_D2", "Heating_D3"}), Cooling_devices({ "Cooling_D1", "Cooling_D2", "Cooling_D3" }), Heating_devices_sts(), Cooling_devices_sts(), Temp_Low_Limit(0), Temp_High_Limit(0), STM("Standby"), HVAC_waiting_Timer(0), HVAC_ERR_Sts("OK")
{

}

bool HVAC::Set_Heating_ON(string device)
{
	return 0;
}
bool HVAC::Set_Heating_OFF(string device)
{
	return 0;
}
bool HVAC::Set_Colling_ON(string device)
{
	return 0;
}
bool HVAC::Set_Colling_OFF(string device)
{
	return 0;
}
string HVAC::HVAC_STM(string state, double Temp)
{
	string STM_sts = state;
	if (state == "Standby")
	{
		if (Temp > Temp_High_Limit)
		{
			STM_sts = "cooling_Wait";
		}
		else if (Temp < Temp_Low_Limit)
		{
			STM_sts = "Heating_Wait";
		}
		else
		{
			STM_sts = "Standby";
		}
	}
	else if (state == "cooling_Wait")
	{
		if (HVAC_waiting_Timer == 0)
		{
			// TODO raise Alarm
		}
		else
		{
			if (HVAC_waiting_Timer >= HVAC_Alarm_Limit)
			{
				STM_sts = "cooling";
			}
			else
			{
				STM_sts = "cooling_Wait";
			}
		}
	}
	else if (state == "Heating_Wait")
	{
		if (HVAC_waiting_Timer == 0)
		{
			// TODO raise Alarm
		}
		else
		{
			if (HVAC_waiting_Timer >= HVAC_Alarm_Limit)
			{
				STM_sts = "Heating";
			}
			else
			{
				STM_sts = "Heating_Wait";
			}
		}
	}
	else if (state == "Heating" || state == "cooling")
	{
		if (Temp > Temp_High_Limit && Temp > Temp_Low_Limit && HVAC_ERR_Sts == "OK")
		{
			STM_sts = "Standby";
		}
		else if (HVAC_ERR_Sts == "NOK")
		{
			STM_sts = "ERR_H";
		}
		else
		{
			// TODO: Rase error
		}
	}
	else if (state == "ERR_H")
	{
		// TODO: check error handler status and select the next state
	}
	else
	{
		// TODO Raise error
	}
	return STM_sts;
}
string HVAC::Get_HVAC_sts()
{
	return STM;
}

bool HVAC::HVAC_Set_Temp_limits(double High, double Low)
{
	return 0;
}


void HVAC::HVAC_Task()
{
	Temprature T;
	double Temp = 0; 
	Temp = T.Get_current_Temp("Indoor");
	STM = HVAC_STM(STM,Temp);

	if (Temp > 10)
	{
		Get_HVAC_sts();
		cout << "Tamp Grater than 10" << endl;

	}
	else
	{
		Get_HVAC_sts();
		cout << "Tamp less than 10" << endl;
	}
}

