import random
from . import __googlesheets

def get (request):
  text = request.args.get('text')
  seed = request.args.get('seed')
  
  hashed_num = custom_hash(text, seed)
  
  all_spells = __googlesheets.get_values("Spells")
  incantations = []
  
  for spell in all_spells:
    if spell[2] == 'y': incantations.append(spell)
    
  # add some blanks so that some results aren't incantations:
  for i in range(0, len(incantations) //2 ):
    incantations.append(['Not an incantati  on', '-', '-', '-', '-'])
  
  return incantations[hashed_num % len(incantations)]

def custom_hash(text, seed):
  random.seed(seed)
  total = 0
  indexfactor = 1
  for ch in text:
    total += ord(ch)**random.randint(3, 5) + random.randint(indexfactor**random.randint(2, 3), indexfactor**random.randint(4, 6)) * 1000
    indexfactor += 1
    
  return total

  
