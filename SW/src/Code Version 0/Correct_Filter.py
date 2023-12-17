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
#from DTC import DHT_DIAG_Update
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
	lenth =len(List)
	List_1=[]
	List_1_2=[]
	print("list lenth")
	print(lenth)
	for i in range(lenth):
		value_1=List[i][1]+List[i][2]
		value_2=List[i][5]+List[i][6]
		List_1.append(value_1)
		List_1.append(value_2)
	print("List after restructure")
	print(List_1)
	while(", " in List_1):
		List_1.remove(", ")
	print("List after restructure and remove elements")
	print(List_1)
	return List_1


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
		diff[0] = round(diff[0],0)
		combination_dict.update({str(ombination_list[i]):abs(diff[0])})
		
	print("combination and diff")
	print(combination_dict)
	# execlude all difference < factor 
	combination_dict= {key:val for key, val in combination_dict.items() if val > Factor_value}
	print("after # execlude all difference > factor ")
	print(combination_dict)
	# make list of sensors repeate in error 
	Error_List=combination_dict.keys()
	print("List of Error List")
	most_frequent_List = most_frequent(Restructure_List(list(Error_List)))
	return most_frequent_List
	
def check_for_deletation(reading,Error,factor):
	counter=0
	Rtn_Flag =0
	for key, val in reading.items():
		if abs((int(Error) - int(val))) >= factor:
			counter=counter+1
		if counter >2 :
			Rtn_Flag =1
		else:
			Rtn_Flag =0
	return Rtn_Flag , Error


def clear_reading_and_LOG_DTC(Dictionary,value):
	try:
		if str(Dictionary["Sensor 1"]) == str(value):
			del Dictionary["Sensor 1"]
			#DHT_DIAG_Update("DTC_7");
	except:
		pass
	try:	
		if str(Dictionary["Sensor 2"]) == str(value):
			del Dictionary["Sensor 2"]
			#DHT_DIAG_Update("DTC_8");
	except:
		pass
	try:	
		if str(Dictionary["Sensor 3"]) == str(value):
			del Dictionary["Sensor 3"]
			#DHT_DIAG_Update("DTC_9");
	except:
		pass
	try:	
		if str(Dictionary["Sensor 4"]) == str(value):
			del Dictionary["Sensor 4"]
			#DHT_DIAG_Update("DTC_10");
	except:
		pass
	try:	
		if str(Dictionary["Sensor 5"]) == str(value):
			del Dictionary["Sensor 5"]
			#DHT_DIAG_Update("DTC_11");
	except:
		pass
	try:	
		if str(Dictionary["Sensor 6"]) == str(value):
			del Dictionary["Sensor 6"]
			#DHT_DIAG_Update("DTC_12");
	except:
		pass
	return Dictionary

def Correct_factor_runable(reading , Factor_value):
	print("The original dictionary is : " + str(reading))
	Rading_correction = reading
	if len(Rading_correction) <3:
		return Rading_correction
	# delete reading 
	deleted_reading = Main_function(Rading_correction,Factor_value)
	while True:
		deleted_reading = Main_function(Rading_correction,Factor_value)
		print("back from main function")
		print(deleted_reading)
		check_Flag ,Error =check_for_deletation(Rading_correction , deleted_reading , Factor_value)
		print("which to delete")
		print(check_Flag ,Error)
		if check_Flag == 1 :
			print("in looooooop check flag comming")
			print("The original dictionary is : " + str(Rading_correction))
			Rading_correction = clear_reading_and_LOG_DTC(Rading_correction,Error)
			#Rading_correction = {key:val for key, val in Rading_correction.items() if val != Error}
			print("dictionary after delete")
			print(Rading_correction)
		else:
			print("out of looooooop ")
			break
	return Rading_correction
	print("############################################################")	

