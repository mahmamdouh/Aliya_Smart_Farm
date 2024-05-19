#include "Sensor_H.h"
using std::vector;
using std::string;
using std::to_string;

using namespace std;

Temp_Sensor::Temp_Sensor() : CurrentTemprature(20)
{

}

double Temp_Sensor::Read_Temp()
{
	return 10;
}

vector <double>  Temp_Sensor::SENSOR_H_get_temp(char Num_reading, string Type)
{
	vector <double> Temprature;
	for (int i = 0; i <= Num_reading; i++)
	{
		Temprature.push_back(Read_Temp());
	}
	return Temprature;
}
