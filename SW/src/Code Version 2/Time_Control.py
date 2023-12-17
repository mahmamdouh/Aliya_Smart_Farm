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
##	component name : Time COntrol       						##
##	Author         : Mahmoud Elmohtady							##
##	Date           : 31/12/2021									##
##																##
##																##
##################################################################
import time
import datetime
from datetime import datetime


Five_Minuts = {
  "Flag": False,
  "Previous": 0,
  "Now": 0,
  "Start_Flag": 0,
}
def Timer_Start():
    today_date = datetime.now()
    hournw =int(today_date.hour)
    miunw  =int(today_date.minute)
    secondd  =int(today_date.second)
    #print(miunw)
    miunwsub=miunw/100
    Five_Minuts["Previous"]=secondd
    Five_Minuts["Start_Flag"] = 1
    
def Timer_Cancel():
    Five_Minuts["Flag"] = True   
    Five_Minuts["Previous"] =0
    Five_Minuts["Now"] =0
    Five_Minuts["Start_Flag"] = 0

def Timer_Check(ratio):
    today_date = datetime.now()
    hournw =int(today_date.hour)
    miunw  =int(today_date.minute)
    secondd  =int(today_date.second)
    Five_Minuts["Now"] =secondd
    if Five_Minuts["Flag"] == False and Five_Minuts["Start_Flag"] ==1:
        if (abs(Five_Minuts["Now"]-Five_Minuts["Previous"]) >= ratio):
            Five_Minuts["Flag"] = True


Air_Time = {
  "Flag": False,
  "Previous": 0,
  "Now": 0,
  "Start_Flag": 0,
}
def Air_Timer_Start():
    today_date = datetime.now()
    hournw =int(today_date.hour)
    miunw  =int(today_date.minute)
    secondd  =int(today_date.second)
    miunwsub=miunw/100
    Air_Time["Previous"]=secondd
    Air_Time["Start_Flag"] = 1
    Air_Time["Flag"] = False 
    
def Air_Timer_Cancel():
    #print("Timer Stop")
    Air_Time["Flag"] = True   
    Air_Time["Previous"] =0
    Air_Time["Now"] =0
    Air_Time["Start_Flag"] = 0

def Air_Timer_Check(ratio):
    today_date = datetime.now()
    hournw =int(today_date.hour)
    miunw  =int(today_date.minute)
    secondd  =int(today_date.second)
    Air_Time["Now"] =secondd
    if Air_Time["Flag"] == False and Air_Time["Start_Flag"] == 1:
        if (abs(Air_Time["Now"]-Air_Time["Previous"]) >= ratio):
            Air_Timer_Cancel()
