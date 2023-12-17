import pickle
from os import path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class Sheets_Logging:
   # The ID and range of a sample spreadsheet.
   SPREADSHEET_ID = '1rBqLyR37LS94M9rOsdJe2P9IRKHPaVp_5w-8i2ZjANY'
   RANGE_NAME = 'Sheet1'
   # If modifying these scopes, delete the file token.pickle.
   SCOPES = ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive.file',
             'https://www.googleapis.com/auth/drive']

   def __init__(self):
       self.service = None
       self.credentials = self.auth()

   def auth(self):
       """Shows basic usage of the Sheets API.
       Prints values from a sample spreadsheet.
       """
       creds = None
       # The file token.pickle stores the user's access and refresh tokens, and is
       # created automatically when the authorization flow completes for the first
       # time.
       if path.exists('token.pickle'):
           with open('token.pickle', 'rb') as token:
               creds = pickle.load(token)
       # If there are no (valid) credentials available, let the user log in.
       if not creds or not creds.valid:
           if creds and creds.expired and creds.refresh_token:
               creds.refresh(Request())
           else:
               flow = InstalledAppFlow.from_client_secrets_file(
                   'credentials.json', self.SCOPES)
               creds = flow.run_local_server(port=0)
           # Save the credentials for the next run
           with open('token.pickle', 'wb') as token:
               pickle.dump(creds, token)
       self.service = build('sheets', 'v4', credentials=creds)

   def read_data(self):
       # Call the Sheets API
       service = self.service
       sheet = service.spreadsheets()
       result = sheet.values().get(spreadsheetId=self.SPREADSHEET_ID,
                                   range=self.RANGE_NAME).execute()
       values = result.get('values', [])
       if not values:
           print('No data found.')
           return None
       else:
           return values

   def write_data(self, data):
       service = self.service
       values = [data]
       body = {
           'values': values
       }
       range_name = 'Sheet1'
       result = service.spreadsheets().values().append(
           spreadsheetId=self.SPREADSHEET_ID, range=range_name,
           valueInputOption='USER_ENTERED', body=body).execute()
       print('{0} cells appended.'.format(result \
                                          .get('updates') \
                                          .get('updatedCells')))