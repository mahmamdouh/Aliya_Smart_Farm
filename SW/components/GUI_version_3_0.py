#!/usr/bin/python3
from tkinter import *                 # imports the Tkinter lib
import RPi.GPIO as GPIO               # imports the GPIO lib
import time
import dht11
import datetime
from datetime import date
from openpyxl import load_workbook
import numpy  # Import numpy 
import matplotlib.pyplot as plt #import matplotlib library 
from drawnow import *

# import time lib
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)               # disable warnings
GPIO.setup(18,GPIO.OUT)		  	          # LED connected to GPIO 23

# read data using pin 14
sensor1 = dht11.DHT11(pin=4)
sensor2 = dht11.DHT11(pin=17)

tempC1 = []     #Empty array 
humidity1 = []
tempC2 = []     #Empty array
tempC3 = []     #Empty array 
humidity2 = []

# sheet data
Temprature1 = ""
Temprature2 = ""
plt.ion() #Tell matplotlib you want interactive mode to plot live data

# create sheet
# Load the workbook and select the sheet
wb = load_workbook('/home/pi/Smart-farm/Smart-farm/SW/Code trial/DHT11_Python/Data/New/weather.xlsx')
sheet = wb['Sheet1']


# DHT11 congig
# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

root = Tk()				     # create the root object
root.wm_title("GUI")			             # sets title of the window
root.configure(bg="#99B897")		       # change the background color 

root.attributes("-fullscreen", True) # set to fullscreen by default

count = 0
def CreatePlot(): #Create a function that makes our desired plot
    plt.subplot(2,1,1)  #Height,Width,First plot
    plt.ylim(22,34)                                 #Set y min and max values
    plt.title('Real Time DHT11 Data')      #Plot the title    
    plt.grid(True)                                  #Turn the grid on    
    plt.ylabel('Temp1 indoor')                            #Set ylabels    
    plt.plot(tempC1,'b^-', label='Degree C')       #plot the temperature  
    plt.legend(loc='upper center')                    #plot the legend
    plt.subplot(2,1,2)  # Height,Width,Second plot
    plt.grid(True)
    plt.ylim(45,70)             #Set limits of second y axis
    plt.plot(tempC1, 'r*-', label='Out door C') #plot humidity data
    plt.plot(tempC2, 'g*-', label='IN door C') #plot humidity data
    plt.ylabel('Temp sensors')    #label second y axis 
    plt.ticklabel_format(useOffset=True)           #to stop autoscale y axis   
    plt.legend(loc='upper center')

# we can exit when we press the escape key
def end_fullscreen(event):
	root.attributes("-fullscreen", False)

def btnClicked():
  if GPIO.input(18):
    GPIO.output(18,GPIO.LOW)
    ledButton["text"]="LED OFF"
  else:
    GPIO.output(18,GPIO.HIGH)
    ledButton["text"]="LED ON"  

def btnExit():
  	root.destroy()



        

label_1 = Label(root, text="Raspberry Pi Graphical User Interface", font="Verdana 26 bold",
			fg="#000",
			bg="#99B898",
			pady = 60,
			padx = 100)

label_2 = Label(root, text="temp", font="Verdana 26 bold",
			fg="#000",
			bg="#99B898",
			pady = 60,
			padx = 100)

label_time = Label(root, text="time", font="Verdana 26 bold",
			fg="#000",
			bg="#99B898",
			pady = 60,
			padx = 100)

label_humid = Label(root, text="humidity", font="Verdana 26 bold",
			fg="#000",
			bg="#99B898",
			pady = 60,
			padx = 100)


exitButton = Button(root, text="Exit", background = "#C06C84",
      command=btnExit, height=10, width=40, font = "Arial 16 bold", activebackground = "red")
	


ledButton = Button(root, text="LED OFF",background = "#C06C84", 
      command=btnClicked, height=10, width=40, font = "Arial 16 bold", activebackground ="#C06C84")


#write temp value
def update():
    time.sleep(1)
    result1 = sensor1.read()
    time.sleep(1)
    result2 = sensor2.read()
    time.sleep(1)
    
    if result1.is_valid():
        print ("getting sensor 1 readings")
        print("Last valid input from sensor 1: " + str(datetime.datetime.now()))
        print("Temperature: %-3.1f C" % result1.temperature)
        print("Humidity: %-3.1f %%" % result1.humidity)
        humidity1.append(result1.humidity)                     #Building our humidity array by appending hum reading
        tempC1.append(result1.temperature)                     #Build our tempC array by appending temp reading        
        today = date.today()
        now = datetime.datetime.now().time()
        #Temprature1 = result1.temperature
        row = (today, now, result1.temperature, result1.humidity)
        
    if result2.is_valid():
        print ("getting sensor 2 readings")
        print("Last valid input from sensor 2: " + str(datetime.datetime.now()))
        print("Temperature: %-3.1f C" % result2.temperature)
        print("Humidity: %-3.1f %%" % result2.humidity)            
        label_2.configure(text=str(result1.temperature)+" C")
        label_time.configure(text=str(datetime.datetime.now()))
        label_humid.configure(text=str(result1.humidity)+ " %")
        tempC3.append(result1.temperature)                     #Build our tempC array by appending temp reading
        ## plotting code
        humidity2.append(result2.humidity)                     #Building our humidity array by appending hum reading
        tempC2.append(result2.temperature)                     #Build our tempC array by appending temp reading
#        time.sleep(1)
        today = date.today()
        now = datetime.datetime.now().time()
        # update data to excel sheet
        #Temprature2 = result2.temperature
        row = (today, now,result1.temperature, result1.humidity,result2.temperature, result2.humidity)
        sheet.append(row)
        # The workbook is saved!
        wb.save('/home/pi/Smart-farm/Smart-farm/SW/Code trial/DHT11_Python/Data/New/weather.xlsx')
        print(tempC1)
        print(tempC2)  
        drawnow(CreatePlot)   
        plt.pause(.000001)
    label_2.after(3000, update)
        
        #time.sleep(3)
        #label_time.after(2000, update)
        #return result.temperature
update()
print("working ...." )

#label_2["text"]=str(result.temperature)
label_time.grid(row=1, column=0)
label_humid.grid(row=2, column=0)

label_1.grid(row=0, column=0)
label_2.grid(row=3, column=0)
exitButton.grid(row = 2 ,column = 1)
ledButton.grid(row = 1 ,column = 1)

root.bind("<Escape>", end_fullscreen)

root.mainloop()				# starts the GUI loop




