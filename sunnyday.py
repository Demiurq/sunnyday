import requests


class Weather:
    """Creates a Weather object getting an apikey as input
    and either a city name or lat and lon coordinates.

    Package use example:

    # Create a weather object using a city name:
    # Get your apikey from https://openweathermap.org
    # And wait a couple of hours for the apikey to be activated

    # weather1 = Weather(apikey = "yourapikeyhere", city = "Rome"

    # Using latitude and longitude coordinates
    # weather2 = Weather(apikey = "yourapikeyhere", lat = 41.1, lon = -4.1)

    # Get complete weather data for the next 12 hours:
    # weather1.next_12h()

    # Simplified data for the next 12 hours:
    # weather1.next_12h_simplified()

    """

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

