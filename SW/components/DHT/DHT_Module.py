import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
sensor1 = dht11.DHT11(pin=4)
sensor2 = dht11.DHT11(pin=27)
sensor3 = dht11.DHT11(pin=22)
sensor4 = dht11.DHT11(pin=23)
sensor5 = dht11.DHT11(pin=24)
sensor6 = dht11.DHT11(pin=25)

# Diag data Base
DHT_DIAG_1 = ""
DHT_DIAG_2 = ""
DHT_DIAG_3 = ""
DHT_DIAG_4 = ""
DHT_DIAG_5 = ""
DHT_DIAG_6 = ""

# Over all Sensor Data
DHT_OverAll_Temp  = 0
DHT_OverAll_humid = 0
DHT_OverAll_Date  = ""



def DHT_Update_10_min():
    time.sleep(1)
    result1 = sensor1.read()
    result2 = sensor2.read()
    result3 = sensor3.read()
    result4 = sensor4.read()
    result5 = sensor5.read()
    result6 = sensor6.read()
    time.sleep(1)

    # take time stamp if current reading
    today = date.today()
    now = datetime.datetime.now().time()


    # data from sensor 1
    if result1.is_valid():
        #DHT_DIAG_Update(1,True)
        DHT_DIAG_1 = True
        print("getting sensor 1 readings")
        print("Last valid input from sensor 1: " + str(datetime.datetime.now()))
        print("Temperature: %-3.1f C" % result1.temperature)
        print("Humidity: %-3.1f %%" % result1.humidity)

    else:
        DHT_DIAG_Update(1, False)

    # data from sensor 2
    if result2.is_valid():
        #DHT_DIAG_Update(2, True)
        DHT_DIAG_2 = True
        print("getting sensor 2 readings")
        print("Last valid input from sensor 2: " + str(datetime.datetime.now()))
        print("Temperature: %-3.1f C" % result2.temperature)
        print("Humidity: %-3.1f %%" % result2.humidity)

    else:
        DHT_DIAG_Update(2, False)

    # data from sensor 3
    if result3.is_valid():
        #DHT_DIAG_Update(3, True)
        DHT_DIAG_3 = True
        print("getting sensor 3 readings")
        print("Last valid input from sensor 3: " + str(datetime.datetime.now()))
        print("Temperature: %-3.1f C" % result3.temperature)
        print("Humidity: %-3.1f %%" % result3.humidity)

    else:
        DHT_DIAG_Update(3, False)

    # data from sensor 4
    if result4.is_valid():
        #DHT_DIAG_Update(4, True)
        DHT_DIAG_4 = True
        print("getting sensor 4 readings")
        print("Last valid input from sensor 4: " + str(datetime.datetime.now()))
        print("Temperature: %-3.1f C" % result4.temperature)
        print("Humidity: %-3.1f %%" % result4.humidity)

    else:
        DHT_DIAG_Update(4, False)

    # data from sensor 5
    if result5.is_valid():
        #DHT_DIAG_Update(5, True)
        DHT_DIAG_5 = True
        print("getting sensor 5 readings")
        print("Last valid input from sensor 5: " + str(datetime.datetime.now()))
        print("Temperature: %-3.1f C" % result5.temperature)
        print("Humidity: %-3.1f %%" % result5.humidity)
    else :
        DHT_DIAG_Update(5, False)

    # data from sensor 6
    if result6.is_valid():
        #DHT_DIAG_Update(6, True)
        DHT_DIAG_6 = True
        print("getting sensor 6 readings")
        print("Last valid input from sensor 6: " + str(datetime.datetime.now()))
        print("Temperature: %-3.1f C" % result6.temperature)
        print("Humidity: %-3.1f %%" % result6.humidity)

    else:
        DHT_DIAG_Update(6, False)

    Temp , Humid = DHT_Algo_calculator()

    return (Temp , Humid)

# function calculate average of data sensor
def DHT_Algo_calculator():
    average = 0
    average=DHT_Get_DIAG_Status()

    DHT_OverAll_Temp = (result1.temperature + result2.temperature + result3.temperature +result4.temperature + result5.temperature + result6.temperature) / average
    DHT_OverAll_humid = (result1.humidity + result2.humidity + result3.humidity +result4.humidity + result5.humidity + result6.humidity) / average
    print("Last valid input from overall: " + str(datetime.datetime.now()))
    return (DHT_OverAll_Temp ,DHT_OverAll_humid)




# function update Diag of DHT sensors
def DHT_DIAG_Update(Diag_num,Diag_status):
    today = date.today()
    now = datetime.datetime.now().time()

    if (Diag_num == 1):
        # update DHT_1 status
        DHT_DIAG_1 = Diag_status

    if (Diag_num == 2):
        # update DHT_2 status
        DHT_DIAG_2 = Diag_status

    if (Diag_num == 3):
        # update DHT_3 status
        DHT_DIAG_3 = Diag_status

    if (Diag_num == 4):
        # update DHT_4 status
        DHT_DIAG_4 = Diag_status

    if (Diag_num == 5):
        # update DHT_5 status
        DHT_DIAG_5 = Diag_status

    if (Diag_num == 6):
        # update DHT_6 status
        DHT_DIAG_6 = Diag_status



#function to GET Diag status
def DHT_Get_DIAG_Status():
    #umber of workign sensors
    num_of_w_sensor =0
    if (DHT_DIAG_1 == False):
        print ("DHT_Sensor 1 have error")
    else:
        num_of_w_sensor=num_of_w_sensor+1

    if (DHT_DIAG_2 == False):
        print ("DHT_Sensor 2 have error")
    else:
        num_of_w_sensor=num_of_w_sensor+1

    if (DHT_DIAG_3 == False):
        print ("DHT_Sensor 3 have error")
    else:
        num_of_w_sensor=num_of_w_sensor+1

    if (DHT_DIAG_4 == False):
        print ("DHT_Sensor 4 have error")
    else:
        num_of_w_sensor=num_of_w_sensor+1

    if (DHT_DIAG_5 == False):
        print ("DHT_Sensor 5 have error")
    else:
        num_of_w_sensor=num_of_w_sensor+1

    if (DHT_DIAG_6 == False):
        print ("DHT_Sensor 6 have error")
    else:
        num_of_w_sensor=num_of_w_sensor+1

    return (num_of_w_sensor)



