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
from HVAC_Controller import Hvac_Set_Limits,Hvac_Get_Limits 
from IO_driver import Heater_1_OFF ,Heater_1_ON ,Heater_2_OFF ,Heater_2_ON ,Heater_3_OFF ,Heater_3_ON ,Collar_1_OFF ,Collar_1_ON ,Collar_2_OFF ,Collar_2_ON ,Collar_3_OFF ,Collar_3_ON
import datetime
import time
from datetime import date
from Sys_Data import Day_Change,HVAC_sys_sts , Get_Date, Room_temp_sts ,time_to_sleep , Ammonia_sts  ,previous ,worksheet , Excel_data_frame ,Operator_HVAC_sys_sts ,Head_count_sts ,Window_2_status ,Day_12_hour,Update_12hur,sys_status,Air_sts,Data,Limits
#from google_spreadsheet import Google_sheet_send_data ,Google_Sheets_Runnable
from DTC import *
from application import App_Main,App_Init,Room_temprate,time_slice,min_Temp_limit_stamp,max_Temp_limit_stamp 
from DTC_Config import read_DTC_Config , config_Update_DTC_data
##################################################################
####               Define Global variable                     ####
##################################################################
counter=0


##################################################################
# Initialization
#mq = MQ();
App_Init()
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
            #print("thread call")
            App_Main()
            time_to_sleep(10)
            ## application code here





################################################################
# main threads
class  MatplotlibWidget ( QMainWindow ):
    
    def  __init__ ( self ):
        #print("clicked in init")
        QMainWindow . __init__ ( self )

        loadUi ( "mainwindow_1.ui" , self )
        
        self.sub_window = SubWindow()
        self.Scaler_Wind1 = Scaler_Wind()
        self.DTC_Window1 = DTC_Window()
        self.Setting1 = Setting()
        self.runTasks()

        #self . setWindowTitle ( "Aliya-co Smart Farm" )
        self . register_2 . clicked . connect ( self . update_graph )
        
        self . ht1_B . clicked . connect ( self . headter_1_control )
        self . ht2_B . clicked . connect ( self . headter_2_control )
        self . ht3_B . clicked . connect ( self . headter_3_control )
        self . co1_B . clicked . connect ( self . cooler_1_control )
        self . co2_B . clicked . connect ( self . cooler_2_control )
        self . co3_B . clicked . connect ( self . cooler_3_control )
        #self . btnOn . clicked . connect ( self . runTasks )
        self . register_2 . clicked . connect (self .Open_operator_window)
        self . Scaler . clicked . connect (self .Open_Scaler_window)
        self . setting . clicked . connect (self .Open_Setting_window)
        self . DTC . clicked . connect (self .Open_DTC_window)
        
        self . Set_Limit . clicked . connect ( self . update_temp_Limit )
        self.Min_Box.valueChanged.connect(self.Min_Box_change)
        self.Max_Box.valueChanged.connect(self.Max_Box_change)
        
        ##################### real time graph
        # calling method Timer
        self.UiTimer()




        #self . addToolBar ( NavigationToolbar ( self . temp_plot . canvas ,  self ))

    def Open_Scaler_window(self):
        self.Scaler_Wind1.show()
        
    def Open_Setting_window(self):
        self.Setting1.show()

    def Open_DTC_window(self):
        self.DTC_Window1.show()

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
        global Room_temprate
        global time_slice
        global min_Temp_limit_stamp
        global max_Temp_limit_stamp
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
        self.Air.setText(str(Air_sts["Condition"]))
        self.Head_count.setText(str(Head_count_sts["Room_head_count"]))
        ############ test code #################33
        #######################################
        
        self . temp_plot . canvas . axes . clear () 
        self . temp_plot . canvas . axes . plot ( time_slice ,  min_Temp_limit_stamp )
        self . temp_plot . canvas . axes . plot ( time_slice ,  max_Temp_limit_stamp )
        self . temp_plot . canvas . axes . plot ( time_slice ,  Room_temprate )
        self . temp_plot . canvas . axes . legend (( 'min' ,  'max' ,'temp'),loc = 'upper right' ) 
        self . temp_plot . canvas . axes . set_title ( ' room temprature' ) 
        self . temp_plot . canvas . draw ()
        
        if Day_Change["Change"] == 1 :
            self . temp_plot . canvas . axes . clear ()
            Room_temprate=[]
            time_slice=[]
            min_Temp_limit_stamp=[]
            max_Temp_limit_stamp=[]
            Day_Change["Change"] = 0
        
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
         self.W2_date.setText(str(date.today()))
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


##  Scaler window
class Scaler_Wind(QMainWindow):
    def __init__(self):
        super(Scaler_Wind, self).__init__()
        loadUi("Scaler.ui", self)

        # variable
        global reading_number
        reading_number = 0
        Current_Reead = 10
        # Label
        self.total_Calculations.setText(str(reading_number))
        # Button
        self.SaveandClose.clicked.connect(self.Close_window)
        self.Next.clicked.connect(self.Update_Scaler_Reqading)
        # spin box
        self.Radingnum.valueChanged.connect(self.Reading_Number)

    def Close_window(self):
        self.close()

    def Update_Scaler_Reqading(self):
        print("iam reading now")
        #reading_number = reading_number - 1
        #Current_Reead = Current_Reead + 10

    def Reading_Number(self, value):
        reading_number = self.Radingnum.value()
        self.total_Calculations.setText(str(reading_number))


## DTC window
class Setting(QMainWindow):
    def __init__(self):
        super(Setting, self).__init__()
        loadUi("Configuration.ui", self)

        # variable
        # Button
        self.C_Save.clicked.connect(self.Close_window)

    def Close_window(self):
        Data["Age"] =self.C_Age.text()
        Data["Head_Cnt"]  =self.C_Head.text()
        Data["Temp_UP"]  =self.C_Temp_U.text()
        Data["Temp_LW"]  =self.C_Temp_L.text()
        Data["Ammonia_L"]  =self.C_Ammonia_L.text()
        Data["Updte_Flag"] = 1
        self.close()

## Setting window
class DTC_Window(QMainWindow):
    def __init__(self):
        super(DTC_Window, self).__init__()
        loadUi("DTC_Window.ui", self)
        self.Update_DTC_Win()
        # variable
        # Button
        self.Close_w.clicked.connect(self.Close_window)
        self.clear_DTC.clicked.connect(self.Clr_Dtc)
        self.Update_DTC.clicked.connect(self.Update_DTC_Win)

    def Close_window(self):
        self.close()
    
    def Update_DTC_Win(self):
        DTC_List =read_DTC_Config()
        self.label1.setText(DTC_List[0])
        self.label2.setText(DTC_List[1])
        self.label3.setText(DTC_List[2])
        self.label4.setText(DTC_List[3])
        self.label5.setText(DTC_List[4])
        self.label6.setText(DTC_List[5])
        self.label7.setText(DTC_List[6])
        self.label8.setText(DTC_List[7])
        self.label9.setText(DTC_List[8])
        self.label10.setText(DTC_List[9])
        self.label11.setText(DTC_List[10])
        self.label12.setText(DTC_List[11])
        self.label13.setText(DTC_List[12])
        self.label14.setText(DTC_List[13])
        self.label15.setText(DTC_List[14])
        self.label16.setText(DTC_List[15])
        self.label17.setText(DTC_List[16])
        self.label18.setText(DTC_List[17])
        self.label19.setText(DTC_List[18])
        self.label20.setText(DTC_List[19])
        self.label21.setText(DTC_List[20])
        self.label22.setText(DTC_List[21])
        self.label23.setText(DTC_List[22])
        self.label24.setText(DTC_List[23])
        self.label25.setText(DTC_List[24])
        self.label26.setText(DTC_List[25])
        self.label27.setText(DTC_List[26])
        self.label28.setText(DTC_List[27])
        self.label29.setText(DTC_List[28])
        self.label30.setText(DTC_List[29])
        self.label31.setText(DTC_List[30])
        self.label32.setText(DTC_List[31])
        self.label33.setText(DTC_List[32])
        self.label34.setText(DTC_List[33])
        self.label35.setText(DTC_List[34])
        self.label36.setText(DTC_List[35])
        self.label37.setText(DTC_List[36])
        self.label38.setText(DTC_List[37])
        self.label39.setText(DTC_List[38])

    def Clr_Dtc(self):
        Clear_Dtc()
        DTC_List = Get_DTC_Sts()
        config_Update_DTC_data(DTC_List)
        self.Update_DTC_Win()

def task ():
	print("print me in task")

if __name__ == '__main__':
	app = QApplication([])
	#form = Form()
	counter=counter+1
	window  =  MatplotlibWidget ()
	#print("clicked")
	#form.setupUi(window)
	window.showFullScreen()
	sys.exit(app.exec())


