import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from father import Ui_MainWindow
from child import Ui_Dialog
 
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.onClicked)
        #Be sure to instantiate the child window in the initialization function of the main window class, if you instantiate the child window in other functions
                 #There may be a problem that the child window crashes
        self.ChildDialog = ChildWin()
 
    def onClicked(self):
                 # print('Open child window!')
        self.ChildDialog.show()
                 #Connect signal
        self.ChildDialog._signal.connect(self.getData)
 
 
    def getData(self, parameter, parameter1):
        # print('This is a test.')
        #print(parameter)
        self.lineEdit.setText(parameter)
        self.lineEdit_2.setText(parameter1)
 
 
class ChildWin(QMainWindow, Ui_Dialog):
         #Define signal
    _signal = QtCore.pyqtSignal(str,str)
    def __init__(self):
        super(ChildWin, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.pushButton.clicked.connect(self.slot1)
 
    def slot1(self):
        data_str = self.lineEdit.text()
        data_str2= self.lineEdit_2.text()
                 #Send signal
        self._signal.emit(data_str,data_str2)
 
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.close()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    ChildWindow = ChildWin()
    MainWindow.show()
    sys.exit(app.exec_())