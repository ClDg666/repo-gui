import requests
import json
from pprint import pprint

APIkey = "d7124f95e99cba247aa9d363b6a8d384"

def city_weather():
    city = input("Enter city: ")
    url = 'http://api.openweathermap.org/data/2.5/weather'
    r = requests.get(url, params={'q': city, 'APPID': APIkey})
    if r.status_code == 200:
        r_json = r.json()
        pprint(r_json)
        path = 'weather_' + str(city) + '.json'
        with open(path, "w") as f:
            json.dump(r.json(), f, indent=2)
        return  r_json
    else:
        print('Name of city is wrong!')

city_weather()
