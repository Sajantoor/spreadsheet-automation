import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import json

pp = pprint.PrettyPrinter()
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

spreadsheetName = 'Python Automation Test Sheet'
sheet = client.open(spreadsheetName).sheet1
teamNames = sheet.col_values(2)
averages = sheet.col_values(3)

data = {}
i = 0

for teams in teamNames:
    data[i].append({'Team': teams}, {'Score'}, averages[i])
    i =+ 1

print(data)
