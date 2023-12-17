############### Application
from urllib.request import urlopen
import xlsxwriter
from datetime import datetime
import pandas as pd
import openpyxl
from Sys_Data import Excel_data_frame


def is_internet_available():
    try:
        urlopen('https://google.com', timeout=1)
        return "internet is Conected"
    except:
        return "internet is not Conected"




def Create_Excel_File(fimename):
    workbook = xlsxwriter.Workbook(fimename)
    worksheet = workbook.add_worksheet()
    workbook.close()
    
Create_Excel_File(file_name)


