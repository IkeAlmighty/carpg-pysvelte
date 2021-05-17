from . import __googlesheets


def get(request):

    tag_type = request.args.get('tagtype')
    if not tag_type: tag_type = "Items"

    all_basic_values = __googlesheets.get_values(tag_type)

    all_tags = []

    for value in all_basic_values:
        value_tags = value[4].split(',')
        for tag in value_tags:
            tag = tag.strip()
            if not tag in all_tags and tag != '-' and tag.upper() != 'NONE':
                all_tags.append(tag)

    return sorted(all_tags)
