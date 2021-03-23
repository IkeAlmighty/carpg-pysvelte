from werkzeug.wrappers import BaseRequest
from . import __googlesheets
import random

'''
Returns a list of items with randomely chose spells and actions on them. 
If 'basic=true' is passed as an request argument, then will return items
without any spells or actions on them. 
'''


def get(request):
    limit = 100
    if request.args.get('limit'):
        limit = int(request.args.get('limit'))
    
    spellchance = 100
    if request.args.get('spellchance'):
        spellchance = int(request.args.get('spellchance'))
        
    basic_items = __googlesheets.rand_basic_values("Items", limit=limit)

    if request.args.get('basic') and request.args.get('basic') == 'true':
        return basic_items
    
    else:  # the default creates full items with spells!
        items = []
        
        # get random spells!
        spells = __googlesheets.rand_basic_values("Spells", limit=limit)
        
        # lower the limit if it is bigger than total item list.
        if limit >= len(basic_items):
            limit = len(basic_items)
        
        # lower the limit if it is bigger than total spell list.
        if limit >= len(spells):
            limit = len(spells)
        
        # populate the items list with items that have spells.
        while len(basic_items) > 0 and len(items) < limit:
            full_item = basic_items.pop(random.randint(0, len(basic_items) - 1))
            
            if random.randint(0, 100) <= spellchance:
                full_item.append(spells.pop(random.randint(0, len(spells) - 1)))
            
            items.append(full_item)
            
        return items
        



