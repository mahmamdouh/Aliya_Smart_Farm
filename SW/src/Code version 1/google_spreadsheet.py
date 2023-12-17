#!/usr/bin/python

# Google Spreadsheet DHT Sensor Data-logging Example

# Depends on the 'gspread' and 'oauth2client' package being installed.  If you
# have pip installed execute:
#   sudo pip install gspread oauth2client

# Also it's _very important_ on the Raspberry Pi to install the python-openssl
# package because the version of Python is a bit old and can fail with Google's
# new OAuth2 based authentication.  Run the following command to install the
# the package:
#   sudo apt-get update
#   sudo apt-get install python-openssl

# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import json
import sys
import time
import datetime


import gspread
from oauth2client.service_account import ServiceAccountCredentials
from Sys_Data import *
from DTC import Google_DIAG_Update
# Type of sensor, can be Adafruit_DHT.DHT11, Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.


# Example of sensor connected to Raspberry Pi pin 23

# Example of sensor connected to Beaglebone Black pin P8_11
#DHT_PIN  = 'P8_11'

# Google Docs OAuth credential JSON file.  Note that the process for authenticating
# with Google docs has changed as of ~April 2015.  You _must_ use OAuth2 to log
# in and authenticate with the gspread library.  Unfortunately this process is much
# more complicated than the old process.  You _must_ carefully follow the steps on
# this page to create a new OAuth service in your Google developer console:
#   http://gspread.readthedocs.org/en/latest/oauth2.html
#
# Once you've followed the steps above you should have downloaded a .json file with
# your OAuth2 credentials.  This file has a name like SpreadsheetData-<gibberish>.json.
# Place that file in the same directory as this python script.
#
# Now one last _very important_ step before updating the spreadsheet will work.
# Go to your spreadsheet in Google Spreadsheet and share it to the email address
# inside the 'client_email' setting in the SpreadsheetData-*.json file.  For example
# if the client_email setting inside the .json file has an email address like:
#   149345334675-md0qff5f0kib41meu20f7d1habos3qcu@developer.gserviceaccount.com
# Then use the File -> Share... command in the spreadsheet to share it with read
# and write acess to the email address above.  If you don't do this step then the
# updates to the sheet will fail!
GDOCS_OAUTH_JSON       = 'google-auth.json'

# Google Docs spreadsheet name.
GDOCS_SPREADSHEET_NAME = 'Aliya-Smart-Farm'

# How long to wait (in seconds) between measurements.

worksheet ={
    "worksheet" : None
}

def login_open_sheet(oauth_key_file, spreadsheet):
    """Connect to Google Docs spreadsheet and return the first worksheet["worksheet"]."""
    try:
        scope =  ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(oauth_key_file, scope)
        gc = gspread.authorize(credentials)
        worksheet["worksheet"] = gc.open(spreadsheet).sheet1
        return worksheet["worksheet"]
    except :
        print('Unable to login and get spreadsheet.  Check OAuth credentials, spreadsheet name, and make sure spreadsheet is shared to the client_email address in the OAuth .json file!')
        print('Google sheet login failed with error:')
        


#print('Logging sensor measurements to {0} every {1} seconds.'.format(GDOCS_SPREADSHEET_NAME, FREQUENCY_SECONDS))
print('Press Ctrl-C to quit.')
worksheet["worksheet"] = None

def Google_sheet_send_data(temp,humid ,ammonia,Air,Hvac,AIR_STM ):
    FREQUENCY_SECONDS     = 10
    # Login if necessary.
    if worksheet["worksheet"] is None:
        worksheet["worksheet"] = login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)

    # Skip to the next reading if a valid measurement couldn't be taken.
    # This might happen if the CPU is under a lot of load and the sensor
    # can't be reliably read (timing is critical to read the sensor).

    #print('Temperature: {0:0.1f} C'.format(temp))


    # Append the data in the spreadsheet, including a timestamp
    #worksheet["worksheet"].append_row((datetime.now().isoformat(), temp,humid ),'RAW',None,"D2:F2")
    try:
        #worksheet["worksheet"].append_row((datetime.datetime.now().isoformat(), temp,humid ),'RAW',None,"D2:F2")
        worksheet["worksheet"].append_row((datetime.now().isoformat(), temp,humid ,ammonia,Air,Hvac,AIR_STM),'RAW',None,"D2:J2")
        worksheet["worksheet"].update('B2',Limits["Temp_Lw_limit"])
        worksheet["worksheet"].update('B3',Limits["Temp_Up_limit"])
        worksheet["worksheet"].update('B4',Limits["Ammonia"])
        worksheet["worksheet"].update('B5',Operator_HVAC_sys_sts["Death"])
        worksheet["worksheet"].update('B6',Head_count_sts["Age"])
        worksheet["worksheet"].update('B7',Operator_HVAC_sys_sts["Food"])


    except:
        # Error appending data, most likely because credentials are stale.
        # Null out the worksheet so a login is performed at the top of the loop.
        print('Append error, logging in again')
        Google_DIAG_Update("DTC_28")
        worksheet["worksheet"] = None
        time.sleep(FREQUENCY_SECONDS)
        

    # Wait 30 seconds before continuing
    print('Wrote a row to {0}'.format(GDOCS_SPREADSHEET_NAME))
    time.sleep(FREQUENCY_SECONDS)


def Google_sheet_Get_data():
    FREQUENCY_SECONDS     = 30
    cell_Data = 0
    Teamp_High =0
    Teamp_Low = 0
    Ammonia_Limit = 0
    Req_Data = []
    # Login if necessary.
    if worksheet["worksheet"] is None:
        worksheet["worksheet"] = login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)

    # Skip to the next reading if a valid measurement couldn't be taken.
    # This might happen if the CPU is under a lot of load and the sensor
    # can't be reliably read (timing is critical to read the sensor).

    #print('Temperature: {0:0.1f} C'.format(temp))


    # Append the data in the spreadsheet, including a timestamp
    try:
        cell_Data = worksheet["worksheet"].get('B9')
        print(cell_Data[0][0])
        Flag = int(cell_Data[0][0])
        if Flag == 1:
            print("I am here")
            Teamp_High = worksheet["worksheet"].get('B2')
            Teamp_Low = worksheet["worksheet"].get('B3')
            Ammonia_Limit = worksheet["worksheet"].get('B4')
            Req_Data.append(Teamp_High[0][0])
            Req_Data.append(Teamp_Low[0][0])
            Req_Data.append(Ammonia_Limit[0][0])
            worksheet["worksheet"].update('B9', 0)
        else:
            return 0


    except:
        # Error appending data, most likely because credentials are stale.
        # Null out the worksheet so a login is performed at the top of the loop.
        print('Append error, logging in again')
        Google_DIAG_Update("DTC_27")
        worksheet["worksheet"] = None
        time.sleep(FREQUENCY_SECONDS)
    return Req_Data


def Google_sheet_send_DTC(DTC):
    FREQUENCY_SECONDS = 10
    # Login if necessary.
    if worksheet["worksheet"] is None:
        worksheet["worksheet"] = login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)

    # Skip to the next reading if a valid measurement couldn't be taken.
    # This might happen if the CPU is under a lot of load and the sensor
    # can't be reliably read (timing is critical to read the sensor).

    # print('Temperature: {0:0.1f} C'.format(temp))

    # Append the data in the spreadsheet, including a timestamp
    # worksheet["worksheet"].append_row((datetime.now().isoformat(), temp,humid ),'RAW',None,"D2:F2")
    try:
        # worksheet["worksheet"].append_row((datetime.datetime.now().isoformat(), temp,humid ),'RAW',None,"D2:F2")
        worksheet["worksheet"].update('B11', DTC[0])
        worksheet["worksheet"].update('B12', DTC[1])
        worksheet["worksheet"].update('B13', DTC[2])
        worksheet["worksheet"].update('B14', DTC[3])
        worksheet["worksheet"].update('B15', DTC[4])
        worksheet["worksheet"].update('B16', DTC[5])
        worksheet["worksheet"].update('B17', DTC[6])
        worksheet["worksheet"].update('B18', DTC[7])
        worksheet["worksheet"].update('B19', DTC[8])
        worksheet["worksheet"].update('B20', DTC[9])
        worksheet["worksheet"].update('B21', DTC[10])
        worksheet["worksheet"].update('B22', DTC[11])
        worksheet["worksheet"].update('B23', DTC[12])
        worksheet["worksheet"].update('B24', DTC[13])
        worksheet["worksheet"].update('B25', DTC[14])
        worksheet["worksheet"].update('B26', DTC[15])
        worksheet["worksheet"].update('B27', DTC[16])
        worksheet["worksheet"].update('B28', DTC[17])
        worksheet["worksheet"].update('B29', DTC[18])
        worksheet["worksheet"].update('B30', DTC[19])
        worksheet["worksheet"].update('B31', DTC[20])
        worksheet["worksheet"].update('B32', DTC[21])
        worksheet["worksheet"].update('B33', DTC[22])
        worksheet["worksheet"].update('B34', DTC[23])
        worksheet["worksheet"].update('B35', DTC[24])
        worksheet["worksheet"].update('B36', DTC[25])
        worksheet["worksheet"].update('B37', DTC[26])
        worksheet["worksheet"].update('B38', DTC[27])
        worksheet["worksheet"].update('B39', DTC[28])
        worksheet["worksheet"].update('B40', DTC[29])
        worksheet["worksheet"].update('B41', DTC[30])
        worksheet["worksheet"].update('B42', DTC[31])
        worksheet["worksheet"].update('B43', DTC[32])
        worksheet["worksheet"].update('B44', DTC[33])
        worksheet["worksheet"].update('B45', DTC[34])
        worksheet["worksheet"].update('B46', DTC[35])
        worksheet["worksheet"].update('B47', DTC[36])
        worksheet["worksheet"].update('B48', DTC[37])
        worksheet["worksheet"].update('B49', DTC[38])



    except:
        # Error appending data, most likely because credentials are stale.
        # Null out the worksheet so a login is performed at the top of the loop.
        print('Append error, logging in again')
        Google_DIAG_Update("DTC_28")
        worksheet["worksheet"] = None
        time.sleep(FREQUENCY_SECONDS)

    # Wait 30 seconds before continuing
    print('Wrote a row to {0}'.format(GDOCS_SPREADSHEET_NAME))
    time.sleep(FREQUENCY_SECONDS)

'''
def Google_Sheets_Runnable(temp,humid ,ammonia ):
    Google_sheet_send_data(temp,humid ,ammonia )
    return Google_sheet_Get_data()
'''
#print(datetime.now().isoformat())
#Google_sheet_send_data(5, 6,7,8,9,10)