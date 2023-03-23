import webbrowser

MAPS_URL = "https://www.google.com/maps/place/"
countries = ["Canada", "Italy", "Cambodia", "Kenya", "Japan"]

for country in countries:
    webbrowser.open_new_tab(MAPS_URL + country)