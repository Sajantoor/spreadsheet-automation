# Python Spreadsheet Automation

### Problem
> In Robotics, our scouts needed to automate the pivot table process due to it taking too long to do manually (we have limited time after scouting process is complete). 

### Imports
```py
import gspread
from gspread_formatting import *
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import json
```

> Gspread is used for Google Sheets API.

### Google Drive API
```py
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
```
> [Google Sheets API](https://developers.google.com/sheets/api) and [Google Drive API](https://developers.google.com/drive) requires client_secret.json credentials.

### How It Works
> Grabs data from the Google Sheets worksheet from specific columns. Using loops it adds up based on team name and averages based on number of times the team appears. Then creates a new worksheet and inputs the data into that 'pivot table' worksheet.

```py
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
```
