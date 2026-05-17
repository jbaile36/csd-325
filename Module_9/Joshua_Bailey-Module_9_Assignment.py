# Joshua Bailey Module 9 Assignment CSD 325 5/17/2026
# This program makes a GET request to the An API of Ice and Fire endpoint,
# for house 4, "House Ambrose", prints the status code of the response, 
# and then prints the JSON data in both raw and formatted forms.

import requests
import json

# Makes a GET request to the API endpoint.
response = requests.get("https://anapioficeandfire.com/api/houses/4")

# Prints status code of API response
print(response.status_code)

# Prints JSON data from API response
print(response.json())

# Formatted print of JSON data from API response
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())