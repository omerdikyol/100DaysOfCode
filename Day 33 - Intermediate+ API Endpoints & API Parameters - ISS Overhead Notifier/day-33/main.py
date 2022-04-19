import time

import requests
from datetime import datetime
import smtplib

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# print(response.status_code)
# response.raise_for_status()
#
# data = response.json()  # Getting data
# print(data)
# print(data["iss_position"])
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)

# Response Codes
# 1XX Hold On
# 2XX Here You Go
# 3XX Go Away
# 4XX You Screwed Up
# 5XX Server Screwed Up

MY_LAT = 51.507351
MY_LNG = -0.127758

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

# If the ISS is close to my current position
def is_iss_overhead():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True


# and it is currently dark
def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split('T')[1].split(':')[0])
    sunset = int(data["results"]["sunset"].split('T')[1].split(':')[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    return False



# Then send me an email to tell me to look up.
MY_EMAIL = "adasd@gmail.com"
MY_PASSWORD = "1234567890"
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_PASSWORD,
            msg="Subject:Title\n\nThe ISS is above you in the sky."
        )

# Bonus: Run the code every 60 seconds
