from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from  PyQt5.QtWidgets  import * 
from  PyQt5.uic  import  loadUi

from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )

import  numpy  as  np 
import  random

#Form, Window = uic.loadUiType("mainwindow2.ui")
min=20
max=50
    
class  MatplotlibWidget ( QMainWindow ):
    
    def  __init__ ( self ):
        print("clicked in init")
        QMainWindow . __init__ ( self )

        loadUi ( "C:/Users/melmohta/Desktop/Aliya_Co/ALI-SF/Smart-farm/SW/Code/GUI/SampleProgram/SampleProgram/mainwindow3.ui" , self )

        self . setWindowTitle ( "PyQt5 & Matplotlib Example GUI" )
        self . register_2 . clicked . connect ( self . update_graph )

        self . addToolBar ( NavigationToolbar ( self . temp_plot . canvas ,  self ))


    def  update_graph ( self ):

        #fs  =  500
        #f  =  random . randint ( 1 ,  100 ) 
        #ts  =  1 / fs 
        #length_of_signal  =  100 
        t  =  [1,2,3,4]

        #cosinus_signal  =  np . cos ( 2 * np . pi * f * t ) 
        #sinus_signal  =  np . sin ( 2 * np . pi * f * t )

        self . temp_plot . canvas . axes . clear () 
        self . temp_plot . canvas . axes . plot ( t ,  [50,50,50,50] )
		#self . temp_plot . canvas . axes . plot ( t ,  [25,25,20,25] )		
        self . temp_plot . canvas . axes . plot ( t ,  [20,20,20,20] )
		#self . temp_plot . canvas . axes . plot ( t ,  min ) 
		#self . temp_plot . canvas . axes . plot ( t ,  max ) 
        self . temp_plot . canvas . axes . legend (( 'min' ,  'max' ,'temp'),loc = 'upper right' ) 
		#self . temp_plot . canvas . axes . legend (( 'cosinus' ,  'sinus' ),loc = 'lower right' ) 
        self . temp_plot . canvas . axes . set_title ( ' Cosinus - Sinus Signal' ) 
        self . temp_plot . canvas . draw ()
	
def task ():
	print("print me in task")

if __name__ == '__main__':
	app = QApplication([])
	#form = Form()
	task()
	window  =  MatplotlibWidget ()
	print("clicked")
	#form.setupUi(window)
	window.show()
	app.exec()
	

	


