from . import __googlesheets

def get(request):
    
    limit = request.args.get('limit')
    if not limit: limit = 100 
    else: limit = int(limit)
    
    tags = request.args.get('tags').split(',')
    tags = [tag.strip() for tag in tags]
    
    print(tags)
    
    return __googlesheets.rand_tagged_values("Spells", valid_tags=tags, limit=limit)