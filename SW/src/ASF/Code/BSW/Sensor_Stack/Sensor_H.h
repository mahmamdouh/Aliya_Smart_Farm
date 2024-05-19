// Sensor_H.h : Include file for standard system include files,
// or project specific include files.

#pragma once

#include <iostream>
#include <vector>
#include <string>

using std::vector;
using std::string;

class Temp_Sensor
{
private:
	double CurrentTemprature;
	vector <double> Temprature_Arr;
	double Read_Temp();

public:
	Temp_Sensor();
	vector <double> SENSOR_H_get_temp(char Num_reading, string Type);
};

