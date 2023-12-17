import configparser

def config_Update_data(Data):
    write_config = configparser.ConfigParser()
    section = "Sensor_IP"
    write_config.add_section(section)
    write_config.set(section, "Sensor_1", Data[0])
    write_config.set(section, "Sensor_2", Data[1])
    write_config.set(section, "Sensor_3", Data[2])
    write_config.set(section, "Sensor_4", Data[3])
    write_config.set(section, "Sensor_5", Data[4])
    write_config.set(section, "Sensor_6", Data[5])
    cfgfile = open("IP.ini", 'w')
    write_config.write(cfgfile)
    cfgfile.close()



def read_Data_Config():
    data_List = []
    section = "Sensor_IP"
    read_config = configparser.ConfigParser()
    read_config.read("IP.ini")
    data_List.append(read_config.get(section, "Sensor_1"))
    data_List.append(read_config.get(section, "Sensor_2"))
    data_List.append(read_config.get(section, "Sensor_3"))
    data_List.append(read_config.get(section, "Sensor_4"))
    data_List.append(read_config.get(section, "Sensor_5"))
    data_List.append(read_config.get(section, "Sensor_6"))
    return (data_List)

print(read_Data_Config())