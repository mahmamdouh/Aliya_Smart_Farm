
import time
import datetime
from datetime import datetime






def Get_Valid_Readings(Reading):
	delited_Key = []
	y = len(Reading)
	for key in Reading:
		if Reading[key] == 0:
			delited_Key.append(key)
	x= len(delited_Key)
	for i in range(x):
		del Reading[delited_Key[i]]
	
	valid_Reading_Nubmer = y-x
	return (Reading,valid_Reading_Nubmer)
	

