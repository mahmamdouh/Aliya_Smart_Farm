
import time
import datetime
from datetime import datetime



Temp_Data = {
    "Sensor1": 0,
    "Sensor2": 2,
    "Sensor4": 6,
    "Sensor5": 5,

}
#    "Sensor6": 0,
def Get_Sensor_Out_Of_Range(Reading):
	delited_key = []
	key = "Sensor1"
	if key in Reading:
		pass
	else:
		delited_key.append("DTC_34")
	key = "Sensor2"
	if key in Reading:
		pass
	else:
		delited_key.append("DTC_35")
	key = "Sensor3"
	if key in Reading:
		pass
	else:
		delited_key.append("DTC_36")
	key = "Sensor4"
	if key in Reading:
		pass
	else:
		delited_key.append("DTC_37")
	key = "Sensor5"
	if key in Reading:
		pass
	else:
		delited_key.append("DTC_38")
	key = "Sensor6"
	if key in Reading:
		pass
	else:
		delited_key.append("DTC_39")
		
	return delited_key
	
	
print(Get_Sensor_Out_Of_Range(Temp_Data))