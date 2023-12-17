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
#from PI_Cam import Image



################################################################
# main threads
class  MatplotlibWidget ( QMainWindow ):
    
    def  __init__ ( self ):
        print("clicked in init")
        QMainWindow . __init__ ( self )

        loadUi ( "C:\Users\melmohta\Desktop\Aliya_Co\IP_Cam_Python_script\GUI\IP_access.ui" , self )
        
        self.sub_window = SubWindow()

        #self . setWindowTitle ( "Aliya-co Smart Farm" )
        #self . pushButton . clicked . connect ( self . runTasks )

		
		
if __name__ == '__main__':
	app = QApplication([])
	#form = Form()
	window  =  MatplotlibWidget ()
	print("clicked")
	#form.setupUi(window)
	window.showFullScreen()
	sys.exit(app.exec())
	

	


