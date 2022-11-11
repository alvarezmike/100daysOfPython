import requests
import config


parameters = {
    "lat": config.latitude,
    "lon": config.longitude,
    "appid": config.api_key,
    "exclude": "current,minute,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

weather_data = [data["hourly"][0]["weather"][0]["id"], data["hourly"][1]["weather"][0]["id"],
data["hourly"][2]["weather"][0]["id"],data["hourly"][3]["weather"][0]["id"],
data["hourly"][4]["weather"][0]["id"],data["hourly"][5]["weather"][0]["id"],
data["hourly"][6]["weather"][0]["id"],data["hourly"][7]["weather"][0]["id"],
data["hourly"][8]["weather"][0]["id"],data["hourly"][9]["weather"][0]["id"],
data["hourly"][10]["weather"][0]["id"],data["hourly"][11]["weather"][0]["id"],
data["hourly"][12]["weather"][0]["id"]]

will_rain = False
print(weather_data)

for i in weather_data:
    if i < 900:
        will_rain = True

if will_rain:
    print("Bring Umbrella")












