
import sys
import RPi.GPIO as GPIO
from time import sleep  
import Adafruit_DHT
import urllib2
import dht11
import time
import datetime


def getSensorData():
	
	# initialize GPIO
	GPIO.setwarnings(True)
	GPIO.setmode(GPIO.BCM) 
	result = instance.read()
        if result.is_valid():
       		 print("Last valid input: " + str(datetime.datetime.now()))

                 print("Temperature: %-3.1f C" % result.temperature) 
				
	time.sleep(6)
			
    # return dict
    return (str(% result.temperature))

# main() function
def main():
	# read data using pin 14
	instance = dht11.DHT11(pin=23)
    # use sys.argv if needed
    if len(sys.argv) < 2:
        print('Usage: python tstest.py PRIVATE_KEY')
        exit(0)
    print 'starting...'

    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % sys.argv[1]

    while True:
        try:
            RH = getSensorData()
            f = urllib2.urlopen(baseURL +
                                "&field1=%s" % (RH))
            print f.read()
            f.close()
            sleep(15)
        except:
            print 'exiting.'
            break

# call main
if __name__ == '__main__':
    main()
