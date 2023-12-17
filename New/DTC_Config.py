import re


DTC_Data ={
	"DTC_1":"0",
	"DTC_2":"0",
	"DTC_3":"0",
	"DTC_4":"0",
	"DTC_5":"0",
	"DTC_6":"0",
	"DTC_7":"0",
	"DTC_8":"0",
	"DTC_9":"0",
	"DTC_10":"0",
	"DTC_11":"0",
	"DTC_12":"0",
	"DTC_33":"0",
	"DTC_13":"0",
	"DTC_14":"0",
	"DTC_17":"0",
	"DTC_18":"0",
	"DTC_19":"0",
	"DTC_20":"0",
	"DTC_21":"0",
	"DTC_22":"0",
	"DTC_23":"0",
	"DTC_24":"0",
	"DTC_42":"0",
	"DTC_36":"0",
	"DTC_37":"0",
	"DTC_38":"0",
	"DTC_39":"0",
	"DTC_40":"0",
	"DTC_41":"0",

	}

def File_create(DTC_Data):
	file1 = open("DTC_Config.txt","w")
	#values = DTC_Data.values() 
	#values_list = list(values)
	L = ["DTC_1="+DTC_Data["DTC_1"],"\nDTC_2="+DTC_Data["DTC_2"],"\nDTC_3="+DTC_Data["DTC_3"],"\nDTC_4="+DTC_Data["DTC_4"],"\nDTC_5="+DTC_Data["DTC_5"],"\nDTC_6="+DTC_Data["DTC_6"],"\nDTC_7="+DTC_Data["DTC_7"],"\nDTC_8="+DTC_Data["DTC_8"],"\nDTC_9="+DTC_Data["DTC_9"],"\nDTC_10="+DTC_Data["DTC_10"],"\nDTC_11="+DTC_Data["DTC_11"],"\nDTC_12="+DTC_Data["DTC_12"],"\nDTC_33="+DTC_Data["DTC_33"],"\nDTC_13="+DTC_Data["DTC_13"],"\nDTC_14="+DTC_Data["DTC_14"],"\nDTC_17="+DTC_Data["DTC_17"],"\nDTC_18="+DTC_Data["DTC_18"],"\nDTC_19="+DTC_Data["DTC_19"],"\nDTC_20="+DTC_Data["DTC_20"],"\nDTC_21="+DTC_Data["DTC_21"],"\nDTC_22="+DTC_Data["DTC_22"],"\nDTC_23="+DTC_Data["DTC_23"],"\nDTC_24="+DTC_Data["DTC_24"],"\nDTC_42="+DTC_Data["DTC_42"],"\nDTC_36="+DTC_Data["DTC_36"],"\nDTC_37="+DTC_Data["DTC_37"],"\nDTC_38="+DTC_Data["DTC_38"],"\nDTC_39="+DTC_Data["DTC_39"],"\nDTC_40="+DTC_Data["DTC_40"],"\nDTC_41="+DTC_Data["DTC_41"]]
	file1.writelines(L)
	file1.close()
	
def File_Get_DTC_Data():
	DTC_Data ={
		"DTC_1":"0",
		"DTC_2":"0",
		"DTC_3":"0",
		"DTC_4":"0",
		"DTC_5":"0",
		"DTC_6":"0",
		"DTC_7":"0",
		"DTC_8":"0",
		"DTC_9":"0",
		"DTC_10":"0",
		"DTC_11":"0",
		"DTC_12":"0",
		"DTC_33":"0",
		"DTC_13":"0",
		"DTC_14":"0",
		"DTC_17":"0",
		"DTC_18":"0",
		"DTC_19":"0",
		"DTC_20":"0",
		"DTC_21":"0",
		"DTC_22":"0",
		"DTC_23":"0",
		"DTC_24":"0",
		"DTC_42":"0",
		"DTC_36":"0",
		"DTC_37":"0",
		"DTC_38":"0",
		"DTC_39":"0",
		"DTC_40":"0",
		"DTC_41":"0",
	}
	file1 = open("DTC_Config.txt","r") 
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_1"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	print("Split data " ,name,DTC_Data["DTC_1"] )

	name,DTC_Data["DTC_2"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_3"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_4"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_5"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_6"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_7"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_8"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_9"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_10"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_11"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_12"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_33"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_13"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_14"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_17"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_18"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_19"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_20"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_21"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_22"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_23"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_24"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_42"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_36"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_37"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_38"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_39"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_40"] =re.split('[=]', Data)
	
	Data =file1.readline()
	Data = Data.rstrip("\n")
	name,DTC_Data["DTC_41"] =re.split('[=]', Data)
	file1.close()
	return DTC_Data


File_create(DTC_Data)

print(File_Get_DTC_Data())
