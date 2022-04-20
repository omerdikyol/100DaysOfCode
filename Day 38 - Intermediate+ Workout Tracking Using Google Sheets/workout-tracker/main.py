import requests
from datetime import datetime
import os

NUTRI_APP_ID = os.environ["NT_APP_ID"]
NUTRI_API_KEY = os.environ["NT_API_KEY"]

AUTH_USERNAME = os.environ["USERNAME"]
AUTH_PASS = os.environ["PASSWORD"]

sheety_post_endpoint = os.environ["SHEETY_ENDP"]

exercise_endpoint = os.environ["EXERCISE_ENDP"]

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 80,
    "height_cm": 193,
    "age": 20
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

current_day = datetime.now().strftime("%d/%m/%Y")
current_hour = datetime.now().strftime("%X")
print(current_day, current_hour)

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date":current_day,
            "time":current_hour,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheety_post_endpoint, json=sheet_inputs, auth=(AUTH_USERNAME, AUTH_PASS))

    print(sheet_response.text)