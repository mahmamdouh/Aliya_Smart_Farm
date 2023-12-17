import Adafruit_DHT  # is a must  
while True:    
    humidity, temperature = Adafruit_DHT.read_retry(11, 23)  # GPIO27 (BCM notation)    
    print ("Humidity = {} %; Temperature = {} C".format(humidity, temperature)) 
