# importing sys
import sys
# adding Folder_2 to the system path
import time
import math
from MCP3008 import MCP3008
import pandas as pd
import openpyxl
from Excel_Local_data import Write_to_Excel_data



Excel_data_frame = pd.DataFrame({'time': [],
                   'temp': []})

counter=0
# Initialization
adc = MCP3008()
while True:
    
    read1 = adc.read(0)
    #print("inloop")
    if read1 != 0:
        print("inloop")
        print(read1)
        counter=counter+1
        Excel_data_frame.loc[len(Excel_data_frame.index)] = [int(counter), int(read1)]
        Write_to_Excel_data(Excel_data_frame)
        time.sleep(100)
        
    

     