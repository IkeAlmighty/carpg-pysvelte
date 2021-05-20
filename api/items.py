from . import __googlesheets
import random

'''
Returns a list of items with randomely chosen spells and actions on them. 
If 'basic=true' is passed as an request argument, then will return items
without any spells or actions on them. 
'''


def get(request):

    def get_query(query_name, default_val):
        if request.args.get(query_name):
            return request.args.get(query_name)
        else:
            return default_val

    limit = int(get_query('limit', 100))
    spellchance = int(get_query('spellchance', 100))
    tags = get_query('tags', '').split(',')

    if request.args.get('seed') and request.args.get('seed') != 'undefined':
        random.seed(request.args.get('seed'))

    if spellchance == 0:
        return __googlesheets.rand_values(__googlesheets.get_values("Items"), limit=limit)

    basic_tagged_items = __googlesheets.rand_tagged_items(
        valid_tags=tags, limit=limit)

    final_items = []

    # get all the spells (randomized)!
    valid_spell_tags = tags.copy()
    # 'any' is not stated explicitely as a tag on items, so we add it.
    valid_spell_tags.append("any")
    tagged_spells = __googlesheets.rand_tagged_spells(
        valid_tags=valid_spell_tags, limit=limit)

    # lower the limit if it is bigger than total item list.
    if limit >= len(basic_tagged_items):
        limit = len(basic_tagged_items)

    # lower the limit if it is bigger than total spell list.
    if limit >= len(tagged_spells):
        limit = len(tagged_spells)

    # populate the final_items list with spell+items with valid tags.
    while len(basic_tagged_items) > 0 and len(final_items) < limit:
        full_item = basic_tagged_items.pop(
            random.randint(0, len(basic_tagged_items) - 1))

        if random.randint(0, 100) <= spellchance:
            full_item.append(tagged_spells.pop(
                random.randint(0, len(tagged_spells) - 1)))

        final_items.append(full_item)

    return final_items
