import requests
from twilio.rest import Client  # Sending SMS
import os

api = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "926e561449071fc317fcf59c604aa0fb"

parameters = {
    "lat": 41.008240,  # Istanbul, TR
    "lon": 28.978359,  # Istanbul, TR
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(api, params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_id = [hour["weather"][0]["id"] for hour in weather_data["hourly"][:12]]
print(weather_id)

will_rain = False
for data in weather_id:
    if int(data) < 700:
        will_rain = True

account_sid = ""
auth_token = ""

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(body="It's going to rain today. Remember to bring an umbrella.", from="my_phone", to="receiver")
    print(message.status)
