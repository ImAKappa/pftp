"""uselessfact.py
This script fetches a useless fact from the useless facts website
"""
from urllib import request
# Data from the internet is passed around in a format called JSON
import json

# Fetch useless fact from some website in JSON form
response = request.urlopen("https://uselessfacts.jsph.pl/api/v2/facts/random")

match response.status:
    case 200:
        # Successful request!
        print("Did you know?")
        # Convert JSON form to something easier to work with in Python
        useless_fact = json.loads(response.read())
        print(useless_fact["text"])
    case 404:
        print("Uh oh, couldn't find a useless fact :(")
    case _:
        # Any other response code is a mystery...
        print("Not sure what happend, but no useless fact :(")