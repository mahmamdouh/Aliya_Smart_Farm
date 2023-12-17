   #!/usr/bin/python3
from tkinter import *                 # imports the Tkinter lib
import RPi.GPIO as GPIO               # imports the GPIO lib
import time
import dht11
import datetime


# import time lib
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)               # disable warnings
GPIO.setup(18,GPIO.OUT)		  	          # LED connected to GPIO 23

# read data using pin 14
instance = dht11.DHT11(pin=4)


# DHT11 congig
# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

root = Tk()				     # create the root object
root.wm_title("GUI")			             # sets title of the window
root.configure(bg="#99B897")		       # change the background color 

root.attributes("-fullscreen", True) # set to fullscreen by default

temp1 =''



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

def update():    
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Humidity: %-3.1f %%" % result.humidity)
        print("Temperature: %-3.1f C" % result.temperature)
        temp1 = str(result.temperature)
        time.sleep(3)
        
def updatetemp():
    if temp1 != '':        
        label_2["text"]=str(temp1)
    else:
        print("NULL")
    
        


label_1 = Label(root, text="Raspberry Pi Graphical User Interface", font="Verdana 26 bold",
        	fg="#000",
        	bg="#99B898",
            pady = 60,
            padx = 100)

label_2 = Label(root, text="temp", font="Verdana 26 bold",
            fg="#000",
            bg="#99B898",
            pady = 60,
            padx = 100,
                command=updatetemp)

exitButton = Button(root, text="Exit", background = "#C06C84",
         command=btnExit, height=10, width=40, font = "Arial 16 bold", activebackground = "red")



ledButton = Button(root, text="LED OFF",background = "#C06C84", 
      command=btnClicked, height=10, width=40, font = "Arial 16 bold", activebackground ="#C06C84")

label_1.grid(row=0, column=0)
label_2.grid(row=3, column=0)
exitButton.grid(row = 2 ,column = 1)
ledButton.grid(row = 1 ,column = 1)
root.bind("<Escape>", end_fullscreen)
    
    
print("working ...." )

update()
print(temp1)
root.mainloop()				# starts the GUI loop
    


    



