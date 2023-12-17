
import sys
import RPi.GPIO as GPIO
from time import sleep  
import dht11
import urllib2



# main() function
def main():

    # initialize GPIO
	GPIO.setwarnings(True)
	GPIO.setmode(GPIO.BCM)

	# read data using pin 14
	instance = dht11.DHT11(pin=14)

    # use sys.argv if needed
    if len(sys.argv) < 2:
        print('Usage: python tstest.py PRIVATE_KEY')
        exit(0)
    print 'starting...'

    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % sys.argv[1]

    while True:
        try:
            result = instance.read()
            if result.is_valid():
                print("Last valid input: " + str(datetime.datetime.now()))

                print("Temperature: %-3.1f C" % result.temperature)
                print("Humidity: %-3.1f %%" % result.humidity)
				RH = result.temperature
				T = result.humidity

            
            f = urllib2.urlopen(baseURL +
                                "&field1=%s&field2=%s" % (RH, T))
            print f.read()
            f.close()
            time.sleep(6)
        except:
            print 'exiting.'
            break

# call main
if __name__ == '__main__':
    main()
