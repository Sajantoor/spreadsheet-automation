# pip install gspread oauth2client
# pip install gspread-formatting
import gspread
from gspread_formatting import *
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

def createWorksheet(name):
    try:
        worksheet = sh.add_worksheet(title=name, rows="200", cols="5")
    except:
        print("The worksheet called " + name +  " already exists!")
        x = input("Call it something else: ")
        createWorksheet(x)
        return


    i = 1
    for team in data:
        worksheet.update_cell(i, 1, team)
        worksheet.update_cell(i, 2, data[team])
        i += 1

    fmt = cellFormat(
        backgroundColor=color(1, 0.9, 0.9),
        textFormat=textFormat(bold=True),
        horizontalAlignment='CENTER'
    )

    format_cell_ranges(worksheet, [('A1:B1', fmt)])
    set_frozen(worksheet, rows=1)

i = 0
for team in teamNames:
    team = team.upper()

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

createWorksheet("Pivot Table")

print("Data added!")
