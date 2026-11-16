import requests
import json
import sys
import datetime as dt
import os
import textwrap
import datetime
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
locationInput = input("What city's weather would you like to look at?")
#Calls the Geocoding API to determine the longitude and lattitude of a given city
url = f"http://api.openweathermap.org/geo/1.0/direct?q={locationInput}&limit=1&appid={api_key}"
httpResponse = requests.get(url)
#print(json.dumps(httpResponse.json(),indent=3))
if httpResponse.status_code == 200:
    data = httpResponse.json()
    if len(data):
        coordinates = dict()
        coordinates['lat']= data[0]['lat']
        coordinates['lon']=data[0]['lon']
    else:
        sys.exit(f"Location not found for {locationInput}. Please re-run the program")
else:
    sys.exit(f"{httpResponse.status_code} {httpResponse.reason}")

latitude = str(coordinates['lat'])
longitude = str(coordinates["lon"])
count = 8
url = f"https://api.openweathermap.org/data/2.5/forecast?cnt={count}&units=imperial&lat={latitude}&lon={longitude}&appid={api_key}"
httpResponse = requests.get(url)
if httpResponse.status_code != 200:
    sys.exit(f"{httpResponse.status_code} {httpResponse.reason}")

#print(json.dumps(httpResponse.json(),indent=3))
print(f"{3 * count}-houre forecast for {httpResponse.json()["city"]["name"]} (3-hour increments):")

for x in httpResponse.json()["list"]:
    print(textwrap.dedent(f'''
        {datetime.datetime.fromtimestamp(x["dt"]).strftime("%a, %b %#d, %Y, %#I:%M %p")}
        Condition: {"/".join(list(map(lambda x: x["main"], x["weather"])))}
        Temp: {round(x["main"]["temp"])}°F
        Feels like: {round(x["main"]["feels_like"])}°F
        Low temp: {round(x["main"]["temp_min"])}°F
        High temp: {round(x["main"]["temp_max"])}°F
        Humidity: {round(x["main"]["humidity"])}%       
    '''))

















