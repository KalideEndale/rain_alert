import requests
from twilio.rest import Client
#use London -0.118092
LON = int(input("What is the Longitude? ")
#use London 51.509865
LAT = int(input("What is the Latitude? ")

# api key
api_key = "REDACTED"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "REDACTED"
auth_token = "REDACTED"

weather_params = {
 "lat": LAT,
 "lon": LON,
 "exclude": "current,minutely, daily",
 "appid": api_key
}

weather_update = requests.get(url=OWM_endpoint, params=weather_params)
weather_update.raise_for_status()
weather_data = weather_update.json()


hourly_weather_data = weather_data["hourly"]
x = slice(12)
twelve_hr_weather_data = hourly_weather_data[x]
print(twelve_hr_weather_data)

will_rain = False
id = []

for hour_data in twelve_hr_weather_data:
    condition_code = hour_data['weather'][0]
    condition_id = condition_code['id']
    id.append(condition_id)
    if condition_id < 700:
        will_rain = True
    else:
        pass

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's expected to rain today, make sure to bring an umbrella! ☔ ",
        from_='+1REDACTED',
        to='+1REDACTED'
    )

print(message.status)
