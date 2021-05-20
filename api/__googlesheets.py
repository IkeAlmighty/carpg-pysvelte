import random
import json
import requests
SPREADSHEET_ID = "1mPBE8TY8fH2ckSRGFazA9cPbNSmx6-DNVrwMJczD-6Q"
GOOGLE_SHEETS_API_KEY = "AIzaSyAaRHCsvBq6T_lj-gfzOFoHiycCnpvBueY"


'''
@param: sheet_tab - the sheet tab name (Items, Spells)
@param: limit - the number of rows of data to return.
Returns a list containing a list for each row of the spreadsheet (matrix).
The spreadsheet can be found at 
https://docs.google.com/spreadsheets/d/1mPBE8TY8fH2ckSRGFazA9cPbNSmx6-DNVrwMJczD-6Q/edit#gid=0
Additions are welcome!!
'''


def get_values(value_type):
    res = requests.get(
        "https://sheets.googleapis.com/v4/spreadsheets/{}/values/{}!A2:E?key={}".format(
            SPREADSHEET_ID,
            value_type,
            GOOGLE_SHEETS_API_KEY
        )
    )
    return json.loads(res.content)["values"]


def rand_basic_values(value_type, limit=None):
    # get a list of all the items.
    all_basic_values = get_values(value_type)
    basic_values = rand_values(all_basic_values, limit=limit)

    return basic_values


'''
    Returns random values within a max limit that have the specified valid_tags.
'''


def rand_tagged_items(valid_tags, limit=None):
    # note: value == "Spells" or "Items"

    # get all items:
    all_basic_items = get_values("Items")

    # filter out items that don't have tags specified by valid_tags
    valid_items = []

    for item in all_basic_items:
        item_tags = item[4].split(',')
        for item_tag in item_tags:
            if item_tag.strip() in valid_tags or 'none' in valid_tags:
                valid_items.append(item)
                break

    return rand_values(valid_items, limit=limit)


def rand_tagged_spells(valid_tags, limit=None, only_incantations=False):
    # get all spells:
    all_spells = get_values("Spells")

    valid_spells = []

    # otherwise, filter out spells that don't have tags specified by valid tags
    for spell in all_spells:
        spell_tags = spell[4].split(',')
        for spell_tag in spell_tags:
            if spell_tag.strip() in valid_tags or "any" in valid_tags:
                if only_incantations and spell[2] == 'y':
                    valid_spells.append(spell)
                    break
                elif not only_incantations and spell[2] == 'n':
                    valid_spells.append(spell)
                    break

    return rand_values(valid_spells, limit=limit)


'''
    Returns random values within a max limit.
'''


def rand_values(values, limit=None):
    _values = values.copy()
    final_values = []

    # lower limit if it is bigger than the dataset (or set it if it is None):
    if limit == None or limit >= len(_values):
        limit = len(_values)

    # randomly populate the list to the right size:
    while len(_values) > 0 and len(final_values) < limit:
        final_values.append(_values.pop(random.randint(0, len(_values) - 1)))

    return final_values
