import requests
from datetime import datetime
import time as time

MY_LAT = -13 # Your latitude
MY_LONG = -73# Your longitude

def isOverhead():
    #get iss position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #get sunset and sunrise
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


    #calculate distance
    distance_lat =  iss_latitude - MY_LAT
    distance_long = iss_longitude - MY_LONG

    #is it above us
    time_now_hour = datetime.now().hour
    print(f"iss_longitude: {iss_longitude}",f"iss_latitude: {iss_latitude}")
    print(f"My longitude: {MY_LONG}", f"My latitude {MY_LAT}")
    if -5 <= distance_lat <= 5 and -5 <= distance_long <= 5:
        if sunset <= time_now_hour <= sunrise:
            print("look up")
    else:
        print("Nope")

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
counter = 0
while True:
    print(counter)
    isOverhead()
    time.sleep(5)
    counter += 1
