# pip install gspread oauth2client
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import json

pp = pprint.PrettyPrinter()
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

spreadsheetName = 'Python Automation Test Sheet'
sh = client.open(spreadsheetName)
sheet = sh.sheet1
teamNames = sheet.col_values(2)
averages = sheet.col_values(3)

data = {}

freq = {}

i = 0
for team in teamNames:
    if team in data:
        data[team] = str(float(data[team]) + float(averages[i]))
        freq[team] = freq[team] + 1
    else:
        data[team] = averages[i]
        freq[team] = 1
    i += 1


for count in freq:
    if (int(freq[count]) > 1):
        data[count] = str(float(data[count]) / int(freq[count]))

worksheet = sh.add_worksheet(title="Pivot Table", rows="200", cols="5")

i = 1
for team in data:
    worksheet.update_cell(i, 1, team)
    worksheet.update_cell(i, 2, data[team])
    i += 1


print(freq)
print(data)
