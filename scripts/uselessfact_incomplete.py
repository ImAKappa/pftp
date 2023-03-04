"""uselessfact.py

This script fetches a useless fact from the useless facts website
"""
from urllib import request
# Data from the internet is passed around in a format called JSON
import json

# Fetch useless fact from some website in JSON form
response = request.urlopen("https://uselessfacts.jsph.pl/api/v2/facts/random")

if response.status == ???:
    # Successful request!
    print("Did you know?")
    # Convert JSON form to something easier to work with in Python
    useless_fact = json.loads(response.read())
    print(useless_fact["text"])
elif response.status == ???:
        print("Uh oh, couldn't find a useless fact :(")
else:
    # Any other status code is a mystery...
    print("Not sure what happend, but no useless fact :(")