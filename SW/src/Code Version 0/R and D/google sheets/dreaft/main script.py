from os import popen
from random import randrange
from datetime import datetime
from Google_Sheets import *


temp = 50

def gen_data():
    temp = measure_temp()
    random_number = randrange(100)
    date = datetime.now()
    return [str(date).split('.')[0], random_number, temp]

if __name__ == '__main__':
    doc = Sheets_Logging()
    data = gen_data()
    doc.write_data(data=data)