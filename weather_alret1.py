# weather dated from https://openweathermap.org/api
# Country codes https://www.iso.org/obp/ui/#search
# find current lat lon: https://www.latlong.net
# View Json weather data: http://jsonviewer.stack.hu

# Dependicies 
import requests
from datetime import datetime
import time

apy_key = ""

OWM_Endpoint = "http://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": 46.309460,
    "lon": -79.461632,
    "appid": apy_key,
    "exclude": "current,minutely,daily,"
}

# response = requests.get(OWM_Endpoint, params=weather_params)
# response.raise_for_status()
# weather_data = response.json()
# print(weather_data["hourly"]["0"])

def get_weather():
    will_rain = False
    global weather_params, OWM_Endpoint, apy_key
    response = requests.get(OWM_Endpoint, params=weather_params)
    response.raise_for_status()
    weather_data = response.json()
    # weather_id = (weather_data["hourly"][0]["weather"][0]["id"])
    # a[:stop] to pick the first 11 hours we use 0 - 12 because 12 -1 = 11
    weather_slice = weather_data["hourly"][0:12]
    for hour_data in weather_slice:
        condition_code = hour_data["weather"][0]["id"]
        if int(condition_code)  <= 700:
            will_rain = True
    
    if will_rain:
        print("bring an umbrella.")

    else:
        print("Sunny Skys Ahead")

get_weather()
