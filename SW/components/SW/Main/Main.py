# importing sys
import sys
# adding Folder_2 to the system path
import IO_driver
from HVAC_Controller import Hvac_control,Hvac_Set_Limits,Hvac_Get_Limits
from  DHT_Module import DHT_Update_10_min , DHT_Get_DIAG_Status , DHT_Get_DIAG
import datetime
import time

while True:
    
    
    Temp , Humid = DHT_Update_10_min()
    DHT_Get_DIAG()
    
    print ("over all data ")
    print (Temp , Humid)
    time.sleep(5)