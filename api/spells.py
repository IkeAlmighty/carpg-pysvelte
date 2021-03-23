from . import __googlesheets

def get():
    return __googlesheets.get_values("Spells")