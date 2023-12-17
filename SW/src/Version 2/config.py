import re


Data ={
	"Name" : "Aliya",
	"Date" : "15/11",
    "Age" : "10",
	"Head Cnt" : "500",
	"Temp_UP" : "30",
	"Temp_LW" : "25",
	"Air_UP" : "30",
	"Air_LW" : "2",
	}

def File_create(Data):
	file1 = open("Config.txt","w")
	L = ["Name:"+Data["Name"],"\nDate:"+Data["Date"],"\nAge:"+Data["Age"],"\nHead Cnt:"+Data["Head Cnt"],"\nTemp_UP:"+Data["Temp_UP"],"\nTemp_LW:"+Data["Temp_LW"],"\nAir_UP:"+Data["Air_UP"],"\nAir_LW:"+Data["Air_LW"]] 
	file1.writelines(L)
	file1.close()
	
def File_Get_Data():
	Data ={
	"Name" : "",
	"Date" : "",
	"Head Cnt" : "",
	"Temp_UP" : "",
	"Temp_LW" : "",
	"Air_UP" : "",
	"Air_LW" : "",
	}
	file1 = open("Config.txt","r") 
	data =file1.readline()

	name,Data["Name"] =re.split('[-:]', data)
	
	data =file1.readline()

	name,Data["Date"] =re.split('[-:]', data)
	
	data =file1.readline()

	name,Data["Head Cnt"] =re.split('[-:]', data)
	
	data =file1.readline()

	name,Data["Temp_UP"] =re.split('[-:]', data)
	
	data =file1.readline()

	name,Data["Temp_LW"] =re.split('[-:]', data)
	
	data =file1.readline()

	name,Data["Air_UP"] =re.split('[-:]', data)
	
	data =file1.readline()

	name,Data["Air_LW"] =re.split('[-:]', data)
	file1.close()
	return Data
	



