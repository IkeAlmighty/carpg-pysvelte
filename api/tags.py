from . import __googlesheets


def get(request):
    all_basic_items = __googlesheets.get_values("Items")

    all_tags = []

    for item in all_basic_items:
        item_tags = item[4].split(',')
        for tag in item_tags:
            tag = tag.strip()
            if not tag in all_tags:
                all_tags.append(tag)

    return sorted(all_tags)
