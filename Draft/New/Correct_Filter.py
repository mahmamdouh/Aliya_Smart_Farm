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
##############################################################################################################
from itertools import combinations
import numpy as np
import collections
import re
##################################################################
####               Define Global variable                     ####
##############################################################################################################

##################################################################
####                Function Definition                       ####
##############################################################################################################
#######################################################################3
def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
#######################################################################3

def Restructure_List(List):
	print("List to find",List)
	lenth =len(List)
	List_1=[]
	for i in range(lenth):
		regi = re.findall("\(\d+\.\d+\,", List[i])
		regi = str(regi)
		regi2 = re.findall("\, \d+\.\d+\)", List[i])
		regi2 = str(regi2)
		regi3 = re.findall("\(\d+\,", List[i])
		regi3 = str(regi3)
		regi4 = re.findall("\, \d+\)", List[i])
		regi4 = str(regi4)
		regi_Flag = re.search("\(\d+\.\d+\,", List[i])
		regi_Flag2 = re.search("\, \d+\.\d+\)", List[i])
		regi_Flag3 = re.search("\(\d+\,", List[i])
		regi_Flag4 = re.search("\, \d+\)", List[i])
		print("=========================")
		if regi_Flag:
			Value1 = re.findall("\d+\.\d+",regi)
			List_1.append(Value1[0])
		if regi_Flag2:
			Value2 = re.findall("\d+\.\d+",regi2)
			List_1.append(Value2[0])
		if regi_Flag3:
			Value3 =re.findall("\d+",regi3)
			List_1.append(Value3[0])
		if regi_Flag4:
			Value4 =re.findall("\d+",regi4)
			List_1.append(Value4[0])

	return List_1

def remove_bad_Elements(element):
	if element == ",":
		return 1
	else:
		return 0
#######################################################################3

def Main_function(reading,Factor_value):
	combination_dict = {
			 }
	values = reading.values() 
	values_list = list(values)

	# find sensor combination 
	ombination_list = [i for i in combinations(values_list,2)]

	#Find ombination list lenth 
	combination_lenth = len(ombination_list)

	# create dictionary of combination and diffrence between 
	for i in range(combination_lenth):
		diff = abs(np.diff(ombination_list[i]))
		combination_dict.update({str(ombination_list[i]):abs(diff[0])})
		
	
	# execlude all difference > factor 
	combination_dict= {key:val for key, val in combination_dict.items() if val > Factor_value}


	# make list of sensors repeate in error 
	Error_List=combination_dict.keys()
	print("Error_List" , Error_List)
	#print("restructure list ",Restructure_List(list(Error_List)))
	New_List = Restructure_List(list(Error_List))
	if len(New_List)>2:
		print("Restructure_List" , New_List)
		most_frequent_List = most_frequent(New_List)
		return most_frequent_List
	else:
		return ""
	
def check_for_deletation(reading,Error,factor):
	counter=0
	Rtn_Flag =0
	for key, val in reading.items():
		if abs((float(Error) - float(val))) >= factor:
			counter=counter+1
		if counter >2 :
			Rtn_Flag =1
		else:
			Rtn_Flag =0
	return Rtn_Flag , Error

def Correct_factor_runable(reading , Factor_value):
	print("The original dictionary is : " + str(reading))
	Rading_correction = reading
	
	
	while True:
		deleted_reading = Main_function(Rading_correction,Factor_value)
		print("Value to delete",deleted_reading)
		print("=",deleted_reading,"=")
		if deleted_reading != "":
			print("HIT")
			Rading_correction = {key:val for key, val in Rading_correction.items() if val != float(deleted_reading)}			
		else :
			break
	return Rading_correction
	#print("############################################################")	


