SPREADSHEET_ID = "1mPBE8TY8fH2ckSRGFazA9cPbNSmx6-DNVrwMJczD-6Q"
GOOGLE_SHEETS_API_KEY = "AIzaSyAaRHCsvBq6T_lj-gfzOFoHiycCnpvBueY"

import requests
import json
import random

'''
@param: sheet_tab - the sheet tab name (Items, Spells, Actions)
@param: limit - the number of rows of data to return.
Returns a list containing a list for each row of the spreadsheet (matrix).
The spreadsheet can be found at 
https://docs.google.com/spreadsheets/d/1mPBE8TY8fH2ckSRGFazA9cPbNSmx6-DNVrwMJczD-6Q/edit#gid=0
Additions are welcome!!
'''
def get_values(value_type):
    res = requests.get(
        "https://sheets.googleapis.com/v4/spreadsheets/{}/values/{}!A2:C?key={}".format(
            SPREADSHEET_ID,
            value_type,
            GOOGLE_SHEETS_API_KEY
        )
    )
    return json.loads(res.content)["values"]

def rand_basic_values(value_type, limit=None):
    # get a list of all the items.
    all_basic_values = get_values(value_type)
    basic_values = []

    # lower limit if it is bigger than the dataset (or set it if it is None):
    if limit == None or limit >= len(all_basic_values):
        limit = len(all_basic_values)

    # randomly populate the list to the right size:
    while len(all_basic_values) > 0 and len(basic_values) < limit:
        basic_values.append(all_basic_values.pop(
            random.randint(0, len(all_basic_values) - 1)))

    return basic_values