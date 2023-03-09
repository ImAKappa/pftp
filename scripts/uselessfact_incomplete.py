"""uselessfact.py

This script fetches a useless fact from the useless facts website
"""
from urllib import request
import json

response = request.urlopen("https://uselessfacts.jsph.pl/api/v2/facts/random")

if response.status == ???: # Your code here
    print("Did you know?")
    useless_fact = json.loads(response.read())
    print(useless_fact["text"])
elif response.status == ???: # Your code here
        print("Uh oh, couldn't find a useless fact :(")
else:
    print("Not sure what happend, but no useless fact :(")