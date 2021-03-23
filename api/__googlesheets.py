SPREADSHEET_ID = "1mPBE8TY8fH2ckSRGFazA9cPbNSmx6-DNVrwMJczD-6Q"
GOOGLE_SHEETS_API_KEY = "AIzaSyAaRHCsvBq6T_lj-gfzOFoHiycCnpvBueY"

import requests
import json

'''
Returns a list containing a list for each row of the spreadsheet (matrix).
The spreadsheet can be found at 
https://docs.google.com/spreadsheets/d/1mPBE8TY8fH2ckSRGFazA9cPbNSmx6-DNVrwMJczD-6Q/edit#gid=0
Additions are welcome!!
'''
def get_values(sheet_tab):
    res = requests.get(
        "https://sheets.googleapis.com/v4/spreadsheets/{}/values/{}!A2:C1000?key={}".format(
            SPREADSHEET_ID,
            sheet_tab,
            GOOGLE_SHEETS_API_KEY
        )
    )
    return json.loads(res.content)["values"]