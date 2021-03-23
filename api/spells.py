from . import __googlesheets

def get(request):
    return __googlesheets.get_values("Spells")