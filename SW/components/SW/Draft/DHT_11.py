import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
sensor1 = dht11.DHT11(pin=4)
sensor2 = dht11.DHT11(pin=17)

try:
	while True:
	    result1 = sensor1.read()
	    result2 = sensor2.read()
	    if result1.is_valid():
	        print("Last valid input from sensor 1: " + str(datetime.datetime.now()))

	        print("Temperature: %-3.1f C" % result1.temperature)
	        print("Humidity: %-3.1f %%" % result1.humidity)
	        
	    if result2.is_valid():
	        print("Last valid input from sensor 2: " + str(datetime.datetime.now()))

	        print("Temperature: %-3.1f C" % result2.temperature)
	        print("Humidity: %-3.1f %%" % result2.humidity)

	    time.sleep(6)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()
