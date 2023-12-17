import configparser

def config_Update_data(Data):
    write_config = configparser.ConfigParser()
    section = "Configuration"
    write_config.add_section(section)
    write_config.set(section, "Name", Data[0])
    write_config.set(section, "Date", Data[1])
    write_config.set(section, "Age", Data[2])
    write_config.set(section, "Head_Cnt", Data[3])
    write_config.set(section, "Temp_UP", Data[4])
    write_config.set(section, "Temp_Lw", Data[5])
    write_config.set(section, "Ammonia_L", Data[6])
    cfgfile = open("SubFiles/Config.ini", 'w')
    write_config.write(cfgfile)
    cfgfile.close()



def read_Data_Config():
    data_List = []
    section = "Configuration"
    read_config = configparser.ConfigParser()
    read_config.read("SubFiles/Config.ini")
    data_List.append(read_config.get(section, "Name"))
    data_List.append(read_config.get(section, "Date"))
    data_List.append(read_config.get(section, "Age"))
    data_List.append(read_config.get(section, "Head_Cnt"))
    data_List.append(read_config.get(section, "Temp_UP"))
    data_List.append(read_config.get(section, "Temp_Lw"))
    data_List.append(read_config.get(section, "Ammonia_L"))
    return (data_List)



#print(read_Data_Config())
