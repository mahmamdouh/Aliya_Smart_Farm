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

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets  import *
from PyQt5.QtGui  import * 
from PyQt5.uic  import  loadUi
from PyQt5.QtCore import QObject, QThread, pyqtSignal , QRunnable, Qt, QThreadPool ,QMutex
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )
import  numpy  as  np 
import  random
import pandas as pd

##################################################################
# import app lib
import sys
from HVAC_Controller import Hvac_control,Hvac_Set_Limits,Hvac_Get_Limits ,Limits
from IO_driver import Heater_1_OFF ,Heater_1_ON ,Heater_2_OFF ,Heater_2_ON ,Heater_3_OFF ,Heater_3_ON ,Collar_1_OFF ,Collar_1_ON ,Collar_2_OFF ,Collar_2_ON ,Collar_3_OFF ,Collar_3_ON
from DHT_Module import DHT_Update_10_min
import datetime
import time
from datetime import date
from mq import *
from Sys_Data import HVAC_sys_sts , Get_Date ,Room_temp ,time_stamp , Room_temp_sts ,time_to_sleep ,min_Temp_limit_stamp,max_Temp_limit_stamp , Ammonia_sts  ,previous ,worksheet , Excel_data_frame ,Operator_HVAC_sys_sts ,Head_count_sts ,Window_2_status ,Update_12hur ,Day_12_hour,sys_status
from google_spreadsheet import Google_sheet_send_data ,Google_Sheets_Runnable
from Excel_Local_data import Write_to_Excel_data
#from DTC import Sys_DTC_sts
from application import is_internet_available,Create_Excel_File


##################################################################
####               Define Global variable                     ####
##################################################################
mini=[]
maxi=[]
temp = []     #Empty array 
tsmp=[]
cnt= []
counter=0
Local_Excel_File=str(datetime.date.today())+'.xlsx'
Create_Excel_File(Local_Excel_File)

##################################################################
# Initialization
#mq = MQ();

##################################################################
####                Function Definition                       ####
##################################################################

################################################################
# threads and runnables
#######################################################################
# function name :                                                     #
# Inputs :                                                            #
# Outputs :                                                           #
# Description :                                                       #
# Function Scope : ( Local - External )                               #
# Arch ID :                                                           #
#######################################################################


# 1. Subclass QRunnable
class Runnable(QRunnable):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        # Your long-running task goes here ...
        while True:
            print("thread call")
            Temprat , Humid = DHT_Update_10_min()
            time_stmp = Get_Date()
            #perc = mq.MQPercentage()
            if Temprat != 0 :
                print ("inside else and if ")
                sys_status["application"]="Running"
                Room_temp.append(Temprat)
                time_stamp.append(time_stmp)
                min_Temp_limit_stamp.append(Limits["Temp_Lw_limit"])
                max_Temp_limit_stamp.append(Limits["Temp_Up_limit"])
                Room_temp_sts["Room_temp"] = Temprat
                #Ammonia_sts["Ammonia"] = round(perc["GAS_ammonia"],2)
                previous["previous_temp"] = Room_temp_sts["Room_temp"]
                ## send data to spread sheet
                sys_status["internet_connection"] = is_internet_available()
                if sys_status["internet_connection"] == "Connected":
                    Google_Sheets_Runnable(Temprat ,Humid,Ammonia_sts["Ammonia"] )
                ## Local Excel update data
                Excel_data_frame.loc[len(Excel_data_frame.index)] = [int(time_stmp), int(Temprat)]
                Write_to_Excel_data (Excel_data_frame,Local_Excel_File)
                Hvac_control(Temprat , Humid)
                    
                   
               ###############
            
            print (Temprat , time_stmp )
            time_to_sleep(10)
            ## application code here





################################################################
# main threads
class  MatplotlibWidget ( QMainWindow ):
    
    def  __init__ ( self ):
        print("clicked in init")
        QMainWindow . __init__ ( self )

        loadUi ( "mainwindow5.ui" , self )
        
        self.sub_window = SubWindow()

        #self . setWindowTitle ( "Aliya-co Smart Farm" )
        self . register_2 . clicked . connect ( self . update_graph )
        
        self . ht1_B . clicked . connect ( self . headter_1_control )
        self . ht2_B . clicked . connect ( self . headter_2_control )
        self . ht3_B . clicked . connect ( self . headter_3_control )
        self . co1_B . clicked . connect ( self . cooler_1_control )
        self . co2_B . clicked . connect ( self . cooler_2_control )
        self . co3_B . clicked . connect ( self . cooler_3_control )
        self . btnOn . clicked . connect ( self . runTasks )
        self . register_2 . clicked . connect (self .Open_operator_window)
        self . Set_Limit . clicked . connect ( self . update_temp_Limit )
        self.Min_Box.valueChanged.connect(self.Min_Box_change)
        self.Max_Box.valueChanged.connect(self.Max_Box_change)
        
        ##################### real time graph
        # calling method Timer
        self.UiTimer()




        self . addToolBar ( NavigationToolbar ( self . temp_plot . canvas ,  self ))
        

    def Open_operator_window(self):
        Window_2_status["Window_open"] =1
        Window_2_status["Data_save"] ==0
        self.sub_window.show()
        
    def runTasks(self):
        threadCount = QThreadPool.globalInstance().maxThreadCount()
        #self.label.setText(f"Running {threadCount} Threads")
        pool = QThreadPool.globalInstance()
        runnable = Runnable(1)
        # 3. Call start()
        pool.start(runnable)
  
    # method for widgets
    def UiTimer(self):
  
        # variables
        # count variable
        self.count = 0
  
        # start flag
        self.start = False

        # creating a timer object
        self.timer = QtCore.QTimer(self)
  
        # adding action to timer
        self.timer.timeout.connect(self.update_graph)
  
        # update the timer every tenth second
        self.timer.start(1800)
        

    def  update_graph ( self ):
        #print("iam in timer now")
        #print(Get_Date())
        #### update head count
        Update_12hur()
        if (Window_2_status["Window_closed"] ==1) and  (Window_2_status["Window_open"] ==0) and(Window_2_status["Data_save"] ==1):
            Head_count_sts["Room_head_count"] = Head_count_sts["Room_head_count"] - Operator_HVAC_sys_sts["Death"]
            Operator_HVAC_sys_sts["Death"] = 0
        #################################
        self.message.setText(str(sys_status["internet_connection"]))
        self.message_2.setText(str(sys_status["application"]))
        ######################################
        self.Time_L.setText(str(Get_Date()))
        self.Temp.setText(str(Room_temp_sts["Room_temp"])+"°C")
        self.Ammonia.setText(str(Ammonia_sts["Ammonia"])+" PPM")
        self.Head_count.setText(str(Head_count_sts["Room_head_count"]))
        ############ test code #################33
        #check buffer temp updated ?
        #print("buffer of temp")
        #print(Room_temp)
        #######################################
        self . temp_plot . canvas . axes . clear () 
        self . temp_plot . canvas . axes . plot ( time_stamp ,  min_Temp_limit_stamp )
        self . temp_plot . canvas . axes . plot ( time_stamp ,  max_Temp_limit_stamp )
        self . temp_plot . canvas . axes . plot ( time_stamp ,  Room_temp )
        self . temp_plot . canvas . axes . legend (( 'min' ,  'max' ,'temp'),loc = 'upper right' ) 
        self . temp_plot . canvas . axes . set_title ( ' room temprature' ) 
        self . temp_plot . canvas . draw ()
        
    def  headter_1_control ( self ):
        if HVAC_sys_sts["Heater_1_sts"] == True :
            Heater_1_OFF()
            HVAC_sys_sts["Heater_1_sts"] = False
            self.heater_1_sts.setText("OFF")
            ##set color to lable
            color_effect = QGraphicsColorizeEffect()
            color_effect.setColor(Qt.darkGreen)
            self.heater_1_sts.setGraphicsEffect(color_effect)
        else:
            Heater_1_ON()
            HVAC_sys_sts["Heater_1_sts"] = True
            self.heater_1_sts.setText("ON")
            ##set color to lable
            color_effect = QGraphicsColorizeEffect()
            color_effect.setColor(Qt.darkRed)
            self.heater_1_sts.setGraphicsEffect(color_effect)
            #self.heater_1_sts = Qheater_1_sts('Light red',self)
        
    def  headter_2_control ( self ):
        if HVAC_sys_sts["Heater_2_sts"] == True :
            Heater_2_OFF()
            HVAC_sys_sts["Heater_2_sts"] = False
            self.heater_2_sts.setText("OFF")
            ##set color to lable
            color_effect = QGraphicsColorizeEffect()
            color_effect.setColor(Qt.darkGreen)
            self.heater_2_sts.setGraphicsEffect(color_effect)
        else:
            Heater_2_ON()
            HVAC_sys_sts["Heater_2_sts"] = True
            self.heater_2_sts.setText("ON")
            ##set color to lable
            color_effect = QGraphicsColorizeEffect()
            color_effect.setColor(Qt.darkRed)
            self.heater_2_sts.setGraphicsEffect(color_effect)
            #self.heater_1_sts = Qheater_1_sts('Light red',self)
        
    def  headter_3_control ( self ):
        if HVAC_sys_sts["Heater_3_sts"] == True :
            Heater_3_OFF()
            HVAC_sys_sts["Heater_3_sts"] = False
            self.heater_3_sts.setText("OFF")
            ##set color to lable
            color_effect = QGraphicsColorizeEffect()
            color_effect.setColor(Qt.darkGreen)
            self.heater_3_sts.setGraphicsEffect(color_effect)
        else:
            Heater_3_ON()
            HVAC_sys_sts["Heater_3_sts"] = True
            self.heater_3_sts.setText("ON")
            ##set color to lable
            color_effect = QGraphicsColorizeEffect()
            color_effect.setColor(Qt.darkRed)
            self.heater_3_sts.setGraphicsEffect(color_effect)
            #self.heater_1_sts = Qheater_1_sts('Light red',self)
        
    def  cooler_1_control ( self ):
        if HVAC_sys_sts["cooler_1_sts"] == True :
            Collar_1_OFF()
            HVAC_sys_sts["cooler_1_sts"] = False
            self.cooler_1_sts.setText("OFF")
            ##set color to lable
            color_effect = QGraphicsColorizeEffect()
            color_effect.setColor(Qt.darkGreen)
            self.cooler_1_sts.setGraphicsEffect(color_effect)
        else:
            Collar_1_ON()
            HVAC_sys_sts["cooler_1_sts"] =True
            self.cooler_1_sts.setText("ON")
            ##set color to lable
            color_effect = QGraphicsColorizeEffect()
            color_effect.setColor(Qt.darkRed)
            self.cooler_1_sts.setGraphicsEffect(color_effect)
            #self.heater_1_sts = Qheater_1_sts('Light red',self)
        
    def  cooler_2_control ( self ):
        if HVAC_sys_sts["cooler_2_sts"] == True :
            Collar_2_OFF()
            HVAC_sys_sts["cooler_2_sts"] = False
            self.cooler_2_sts.setText("OFF")
            ##set color to lable
            color_effect = QGraphicsColorizeEffect()
            color_effect.setColor(Qt.darkGreen)
            self.cooler_2_sts.setGraphicsEffect(color_effect)
        else:
            Collar_2_ON()
            HVAC_sys_sts["cooler_2_sts"] =True
            self.cooler_2_sts.setText("ON")
            ##set color to lable
            color_effect = QGraphicsColorizeEffect()
            color_effect.setColor(Qt.darkRed)
            self.cooler_2_sts.setGraphicsEffect(color_effect)
            #self.heater_1_sts = Qheater_1_sts('Light red',self)
        
    def  cooler_3_control ( self ):
        if HVAC_sys_sts["cooler_3_sts"] == True :
            Collar_3_OFF()
            HVAC_sys_sts["cooler_3_sts"] = False
            self.cooler_3_sts.setText("OFF")
            ##set color to lable
            color_effect = QGraphicsColorizeEffect()
            color_effect.setColor(Qt.darkGreen)
            self.cooler_3_sts.setGraphicsEffect(color_effect)
        else:
            Collar_3_ON()
            HVAC_sys_sts["cooler_3_sts"] =True
            self.cooler_3_sts.setText("ON")
            ##set color to lable
            color_effect = QGraphicsColorizeEffect()
            color_effect.setColor(Qt.darkRed)
            self.cooler_3_sts.setGraphicsEffect(color_effect)
            #self.heater_1_sts = Qheater_1_sts('Light red',self)
            
    def Min_Box_change(self,value):
        Limits["Temp_Lw_limit"] =self.Min_Box.value()
        
    def Max_Box_change(self,value):
        Limits["Temp_Up_limit"] =self.Max_Box.value()

    def update_temp_Limit(self):
        self.label_10.setText(str(Limits["Temp_Up_limit"]))
        self.label_9.setText(str(Limits["Temp_Lw_limit"]))



## operator register window
class SubWindow(QMainWindow):
     def __init__(self):
         super(SubWindow, self).__init__()
         loadUi ( "Register_window.ui" , self )

         # Label         
         self . W2_Close . clicked . connect ( self.Close_window )
         self . W2_Save . clicked . connect ( self.Save_Data )
         self.W2_date.setText(str(datetime.date.today()))
         self.W2_Time.setText(str(Get_Date()))
         self.W2_food.valueChanged.connect(self.W2_food_change)
         self.W2_death.valueChanged.connect(self.W2_death_change)
    
    
     def Close_window(self):
         Window_2_status["Window_closed"] =1
         Window_2_status["Window_open"] = 0
         self.close()
         
     def Save_Data(self):
         operator_name_text = self.W2_operator.toPlainText()
         operator_notic = self.W2_notic.toPlainText()
         #W2_operator.textChanged.connect(lambda: print(W2_operator.document().toPlainText()))
         #print(operator_name_text)
         #print(operator_notic)
         Operator_HVAC_sys_sts["Operator_name"] =operator_name_text
         Operator_HVAC_sys_sts["Operator_notic"] = operator_notic
         Window_2_status["Data_save"] =1
         

        
     def W2_food_change(self,value):
        Operator_HVAC_sys_sts["Food"] = Operator_HVAC_sys_sts["Food"] + self.W2_food.value()
        
     def W2_death_change(self,value):
        Operator_HVAC_sys_sts["Death"] = self.W2_death.value()
         






def task ():
	print("print me in task")

if __name__ == '__main__':
	app = QApplication([])
	#form = Form()
	counter=counter+1
	window  =  MatplotlibWidget ()
	print("clicked")
	#form.setupUi(window)
	window.showFullScreen()
	sys.exit(app.exec())
	

	


