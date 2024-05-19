import serial # import Serial Library
import numpy  # Import numpy 
import matplotlib.pyplot as plt #import matplotlib library 
from drawnow import *
tempC = []     #Empty array 
humidity = []
arduino = serial.Serial("/dev/ttyACM0", 115200)   #Serial port to which arduino is connected and Baudrate
plt.ion() #Tell matplotlib you want interactive mode to plot live data
def CreatePlot(): #Create a function that makes our desired plot
    plt.subplot(2,1,1)  #Height,Width,First plot
    plt.ylim(22,34)                                 #Set y min and max values
    plt.title('Real Time DHT11 Data')      #Plot the title
    
    plt.grid(True)                                  #Turn the grid on
    
    plt.ylabel('Temp C')                            #Set ylabels
    
    plt.plot(tempC,'b^-', label='Degree C')       #plot the temperature
  
    plt.legend(loc='upper center')                    #plot the legend
    plt.subplot(2,1,2)  # Height,Width,Second plot

    plt.grid(True)
    plt.ylim(45,70)             #Set limits of second y axis
    plt.plot(humidity, 'g*-', label='Humidity (g/m^3)') #plot humidity data
    
    plt.ylabel('Humidity (g/m^3)')    #label second y axis
  
    plt.ticklabel_format(useOffset=False)           #to stop autoscale y axis
   
    plt.legend(loc='upper center')
while True: # While loop that loops forever
    while (arduino.inWaiting()==0): #Wait here until there is data
        pass #do nothing
  
  arduinoString = arduino.readline() #read the data from serial port
   dataArray = arduinoString.split(',')   #Split it into an array

    temp = float( dataArray[0])            #Convert first element to floating number and put in temp
    hum = float( dataArray[1])            #Convert second element to floating number and put in hum
  
    tempC.append(temp)                     #Build our tempC array by appending temp reading
    
    humidity.append(hum)                     #Building our humidity array by appending hum reading
    
   drawnow(CreatePlot)
    
   plt.pause(.000001)
    
   count=count+1
   if(count>20):    #only take last 20 data if data is more it will pop first
        tempC.pop(0) # pop out first element
        
        humidity.pop(0)