##################################################################
##																##
##		   /\		|		|	\		/		/\				##
##		  /	 \		|		|    \     /	   /  \			    ##
##		 /	  \		|		|	  \   /		  /	   \		    ##
##		/------\	|		|	   \ /	   	 /------\			##
##	   /	 	\	|_____	|	|___/		/		 \			##
## 																##
## 			    	Aliya Smart System							##
## 			         WWW.Aliya-Co.com							##
##################################################################
##################################################################
##  Project        : Aliya-Smart-Farm                           ##
##	component name : Read Correct Filter						##
##	Author         : Mahmoud Elmohtady							##
##	Date           : 31/10/2021									##
##																##
##																##
##################################################################

##################################################################
####                  Liberary Include                        ####
##################################################################

import pandas as pd
import openpyxl
from Sys_Data import Excel_data_frame
from DTC import Excel_DIAG_Update

##################################################################
####                Function Definition                       ####
##################################################################


#######################################################################
# function name :                                                     #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################
def Write_to_Excel_data(data_fame ,file_name):
    try:
        df1 = data_fame
        book = openpyxl.load_workbook(file_name) #Already existing workbook
        writer = pd.ExcelWriter(file_name, engine='openpyxl') #Using openpyxl
        #Migrating the already existing worksheets to writer
        writer.book = book
        writer.sheets = {x.title: x for x in book.worksheets}
        df1.to_excel(writer, sheet_name='Sheet2')
        writer.save()
        writer.close()
    except:
        Excel_DIAG_Update("DTC_25")
    