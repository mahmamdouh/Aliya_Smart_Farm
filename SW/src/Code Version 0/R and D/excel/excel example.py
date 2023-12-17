import pandas as pd
import openpyxl
from Sys_Data import Excel_data_frame


def Write_to_Excel_data(data_fame):   
    df1 = data_fame
    book = openpyxl.load_workbook('Excel_Data.xlsx') #Already existing workbook
    writer = pd.ExcelWriter('Excel_Data.xlsx', engine='openpyxl') #Using openpyxl
    #Migrating the already existing worksheets to writer
    writer.book = book
    writer.sheets = {x.title: x for x in book.worksheets}
    df1.to_excel(writer, sheet_name='Sheet2')
    writer.save()
    writer.close()
    
    