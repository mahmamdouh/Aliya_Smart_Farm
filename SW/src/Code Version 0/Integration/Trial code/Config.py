
#Data=["New_Aliya","27.1.2022","5","70","30","25","10"]


import configparser




def config_Update_data(Data):
	write_config = configparser.ConfigParser()
	section = "Configuration"
	write_config.add_section(section)
	write_config.set(section,"Name",Data[0])
	write_config.set(section,"Date",Data[1])
	write_config.set(section,"Age",Data[2])
	write_config.set(section,"Head_Cnt",Data[3])
	write_config.set(section,"Temp_UP",Data[4])
	write_config.set(section,"Temp_Lw",Data[5])
	write_config.set(section,"Ammonia_L",Data[6])
	cfgfile = open("Config.ini",'w')
	write_config.write(cfgfile)
	cfgfile.close()
	#print(data)


def read_Cam_Config(Sections):
	data_List=[]
	section = "Configuration"
	read_config = configparser.ConfigParser()
	read_config.read("Config.ini")
	data_List.append(read_config.get(section,"Name"))
	data_List.append(read_config.get(section,"Date"))
	data_List.append(read_config.get(section,"Age"))
	data_List.append(read_config.get(section,"Head_Cnt"))
	data_List.append(read_config.get(section,"Temp_UP"))
	data_List.append(read_config.get(section,"Temp_Lw"))
	data_List.append(read_config.get(section,"Ammonia_L"))
	return (data_List)
	
	
config_Update_data(["New_Aliya","27.1.2022","5","70","30","25","10"])



#print(read_Cam_Config("Lap_Top_Cam"))