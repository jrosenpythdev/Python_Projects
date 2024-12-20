import requests
import datetime as dt
import os as os

GENDER = "Male"
WEIGHT_KG = "74"
HEIGHT_CM = 172
AGE = 32



#Nutritionix
APPLICATION_ID = os.environ["APP_ID"]
APPLICATION_KEYS = os.environ["APP_KEYS"]
NUTRI_HOST_DOMAIN = "https://trackapi.nutritionix.com"
NUTRI_ENDPOINT = "/v2/natural/exercise"

#os.environ["APP_ID"] = APPLICATION_ID

print(APPLICATION_ID)
print(APPLICATION_KEYS)


nutri_headers = {
    "x-app-id":APPLICATION_ID,
    "x-app-key":APPLICATION_KEYS,
    "Content-Type": "application/json"
}
exercise_text = input("Tell me which exercises you did: ")
params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

#Sheety
SHEETY_HOST_DOMAIN = "https://api.sheety.co/"
SHEETY_ENDPOINT = "/4081fefc592598f6a0cca7ec9082506b/jamesWorkouts/workouts"

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic amFtZXM6ZHNsa2pkZmxrZHNmbGtqZHNramxsa2pkc2Zsaw=="
}

Eurl=  f"{NUTRI_HOST_DOMAIN}{NUTRI_ENDPOINT}"
       # , json)=params, headers=nutri_headers
nutri_response =  requests.post(Eurl,json = params, headers = nutri_headers).json()

for exercise in nutri_response["exercises"]:
    sheety_body = {
        "workout": {
            "date": dt.datetime.now().strftime("%d/%m/%Y"),
            "time": dt.datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise["user_input"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

sheety_response = requests.post(url = f"{SHEETY_HOST_DOMAIN}{SHEETY_ENDPOINT}",json=sheety_body, headers=sheety_headers)


print(sheety_response.json())
#print(sheety_response.status_code)