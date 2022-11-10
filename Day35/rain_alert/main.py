import requests
import config

parameters = {
    "lon": config.longitude,
    "lat": config.latitude,
    "appid": config.api_key
}

response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
