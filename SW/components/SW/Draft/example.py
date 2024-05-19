import RPi.GPIO as GPIO
import dht11
import time
import datetime
from gpiozero import LED
from time import sleep

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
led = LED(18)

# read data using pin 14
instance = dht11.DHT11(pin=4)

try:
	while True:
            result = instance.read()
            if result.is_valid():
                print("Last valid input: " + str(datetime.datetime.now()))

                print("Temperature: %3.1f C" % result.temperature)
                print("Humidity: %3.1f %%" % result.humidity)

            time.sleep(6)
            if(result.temperature > 18):
                led.on()
                print("led on")
                sleep(1)
            else:
                led.off()
                print("led off")
                sleep(1)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()
