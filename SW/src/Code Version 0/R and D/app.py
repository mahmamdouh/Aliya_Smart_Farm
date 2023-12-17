# importing sys
import sys
# adding Folder_2 to the system path
import IO_driver
from HVAC_Controller import Hvac_control,Hvac_Set_Limits,Hvac_Get_Limits
from  DHT_Module import DHT_Update_10_min , DHT_Get_DIAG_Status , DHT_Get_DIAG
import datetime
import time
from mq import *


# Initialization
mq = MQ();
while True:
    
    perc = mq.MQPercentage()
    Temp , Humid = DHT_Update_10_min()
    #DHT_Get_DIAG()
    
    print ("over all data ")
    print (Temp , Humid)
    #print("Time now  " + str(datetime.datetime.now()))
    print ("===================================================== ")
    Hvac_control(Temp , Humid)
    Hvac_Get_Limits()
    ammonia = perc["GAS_ammonia"]
    sys.stdout.write("NH3: %g ppm" % (perc["GAS_ammonia"]))
    sys.stdout.write("    CO: %g ppm" % (perc["CO"]))
    sys.stdout.write("    Asitona: %g ppm" % (perc["Asitona"]))
    #print(ammonia)
     