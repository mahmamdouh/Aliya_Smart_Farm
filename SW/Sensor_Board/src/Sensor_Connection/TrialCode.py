
import time
import datetime
from datetime import datetime
import pandas as pd
import xlsxwriter
import pandas as pd
import openpyxl



Day_hour = {
  "Today" : 0 ,
  "Last_Day": 0,
  "Num_Of_Days":0,
}
'''	
def Set_Today():
	localtime = time.localtime()
	day = int(localtime.tm_mday)
	Day_hour["Today"] = day
	
	

def Update_Day():
	localtime = time.localtime()
	day = int(localtime.tm_mday)
	if Day_hour["Today"] != Day_hour["Last_Day"] :
		Day_hour["Last_Day"] =Day_hour["Today"]
		Day_hour["Num_Of_Days"]=Day_hour["Num_Of_Days"]+1
		return 1
	else :
		return 0
    
'''




def Create_Excel_File(fimename):
    workbook = xlsxwriter.Workbook(fimename)
    worksheet = workbook.add_worksheet()
    workbook.close()
	
Local_Excel_File = "15-11" + '.xlsx'
Create_Excel_File(("Data/"+Local_Excel_File))