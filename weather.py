import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
API_key = os.getenv('OPENWEATHER_API_KEY')

@dataclass
class WeatherData:
    name: str
    main: str
    description: str
    icon: str
    temperature: int
    temp_min: int
    temp_max: int
    humidity: str


def get_lat_lon(city_name, state_code, country_code, API_key):
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    data = resp[0]
    lat, lon = data.get('lat'), data.get('lon')
    return lat, lon 

def get_current_weather(lat, lon, API_key):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=imperial').json()

    data = WeatherData(
    name=resp.get('name'),
    main=resp.get('weather')[0].get('main'),
    description=resp.get('weather')[0].get('description'),
    icon=resp.get('weather')[0].get('icon'),
    temperature=int(resp.get('main').get('temp')),
    temp_min=int(resp.get('main').get('temp_min')),
    temp_max=int(resp.get('main').get('temp_max')),
    humidity=resp.get('main').get('humidity')
    )

    return data

def main(city_name, state_name, country_name):
    lat, lon = get_lat_lon(city_name, state_name, country_name, API_key)
    weather_data = get_current_weather(lat, lon, API_key)
    name = city_name
    return weather_data

if __name__ == "__main__":
    lat, lon = get_lat_lon()



