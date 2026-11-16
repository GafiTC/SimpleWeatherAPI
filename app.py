import requests
import json
import sys
import datetime as dt
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
location = "New York"
url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={api_key}"
httpResponse = requests.get(url)
print(json.dumps(httpResponse.json(),indent=3))

if httpResponse.status_code == 200:
    data = httpResponse.json()
    if len(data):
        coordinates = dict()
        coordinates['lat']= data[0]['lat']
        coordinates['lon']=data[0]['lon']
    else:
        sys.exit(f"Location not found for {location}")
else:
    sys.exit(f"{httpResponse.status_code} {httpResponse.reason}")

latitude = str(coordinates['lat'])
longitude = str(coordinates["lon"])
count = 8
url = f"https://api.openweathermap.org/data/2.5/forecast?cnt={count}&units=imperial&lat={latitude}&lon={longitude}&appid={api_key}"
httpResponse = requests.get(url)
if httpResponse.status_code != 200:
    sys.exit(f"{httpResponse.status_code} {httpResponse.reason}")

print(json.dumps(httpResponse.json(),indent=3))
print()
print(f"{3 * count}-houre forecast for {httpResponse.json()["city"]["name"]} (3-hour increments):")

















