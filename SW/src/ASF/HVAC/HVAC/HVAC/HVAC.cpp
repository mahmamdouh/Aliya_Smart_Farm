// HVAC.cpp : Defines the entry point for the application.
//

#include "HVAC.h"
#include "Sensor_H.h"
using std::vector;
using std::string;
using std::to_string;

using namespace std;

Temprature::Temprature() : IndoorCurrentTemprature(20), OutdoorCurrentTemprature(20)
{

}

double Temprature::Get_Indoor_Temprature()
{

	return 0;
}
double Temprature::Get_Outdoor_Temprature()
{
	return 0;
}
double Temprature::Temp_equilizer(double temp)
{
	return 0;
}


HVAC::HVAC() : Heating_devices(), Cooling_devices(), Heating_devices_sts(), Cooling_devices_sts()
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
string HVAC::Get_HVAC_sts()
{
	return "NOK";
}
void HVAC::HVAC_Task()
{

}

int main()
{
	cout << "Hello CMake." << endl;
	return 0;
}
