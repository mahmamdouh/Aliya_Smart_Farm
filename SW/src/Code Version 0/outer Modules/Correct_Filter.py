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
	for i in range(lenth):
		value_1=List[i][1]+List[i][2]
		value_2=List[i][5]+List[i][6]
		List_1.append(int(value_1))
		List_1.append(int(value_2))
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
		combination_dict.update({str(ombination_list[i]):abs(diff[0])})
		

	# execlude all difference > factor 
	combination_dict= {key:val for key, val in combination_dict.items() if val > Factor_value}


	# make list of sensors repeate in error 
	Error_List=combination_dict.keys()
	most_frequent_List = most_frequent(Restructure_List(list(Error_List)))
	return most_frequent_List
	
def check_for_deletation(reading,Error,factor):
	counter=0
	Rtn_Flag =0
	for key, val in reading.items():
		if abs((Error - val)) >= factor:
			counter=counter+1
		if counter >2 :
			Rtn_Flag =1
		else:
			Rtn_Flag =0
	return Rtn_Flag , Error

def Correct_factor_runable(reading , Factor_value):
	print("The original dictionary is : " + str(reading))
	Rading_correction = {
			 }
	Rading_correction = reading
	deleted_reading = Main_function(Rading_correction,Factor_value)
	while True:
		deleted_reading = Main_function(Rading_correction,Factor_value)
		#print("input to check")
		#print(deleted_reading)		
		check_Flag ,Error =check_for_deletation(Rading_correction , deleted_reading , Factor_value)
		if check_Flag == 1 :
			Rading_correction = {key:val for key, val in Rading_correction.items() if val != Error}
			
		else:
			break
	return Rading_correction
	print("############################################################")	

