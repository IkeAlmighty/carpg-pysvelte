from . import __googlesheets


def get(request):

    limit = request.args.get('limit')
    if not limit:
        limit = 100
    else:
        limit = int(limit)

    tags = ["any"]
    if request.args.get('tags'):
        tags = request.args.get('tags').split(',')
        tags = [tag.strip() for tag in tags]

    onlyincantations = False
    if request.args.get('onlyincantations'):
        onlyincantations = bool(request.args.get('onlyincantations'))

    return __googlesheets.rand_tagged_spells(valid_tags=tags, limit=limit, only_incantations=onlyincantations)
