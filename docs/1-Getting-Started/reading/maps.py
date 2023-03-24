import webbrowser

maps_url = "https://www.google.com/maps/place/"
countries = ["Canada", "Italy", "Cambodia", "Kenya", "Japan"]

for country in countries:
    webbrowser.open_new_tab(maps_url + country)
