import requests
from pprint import pprint
import os

API = os.getenv("OPENWEATHERAPI")

class Weather:

    def __init__(self, apikey: str, city: str = None, lat: float = None, lon: float = None):
        if city:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=metric"
            request = requests.get(url)
            self.data = request.json()
        elif lat and lon:
            url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apikey}&units=metric"
            request = requests.get(url)
            self.data = request.json()
        else:
            raise TypeError("provide either a city or lat and lon arguments")
        if self.data["cod"] != "200":
            raise ValueError(self.data["message"])

    def next_12h(self):
        return self.data['list'][:4]

    def next_12h_simplified(self):
        simple_data = []
        for dicty in self.data['list'][:4]:
            simple_data.append((dicty['dt_txt'], dicty['main']['temp'], dicty['weather'][0]['description']))
        return simple_data


# weather = Weather(apikey=API, city="Rome")
weather = Weather(apikey=API, city="Rome")
pprint(weather.next_12h_simplified())
