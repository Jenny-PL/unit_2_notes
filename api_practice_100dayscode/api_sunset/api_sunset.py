import requests
from datetime import datetime

SEATTLE_LAT = 47.6
SEATTLE_LONG = -122.3

def get_sunrise_sunset():
    # response = requests.get(url="https://api.sunrise-sunset.org/json?lat=47.6&lng=122.3")
    params = {
        'lat': SEATTLE_LAT,
        'lng': SEATTLE_LONG,
        'formated': 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)

    # the request below should give error, as its missing 2 required params:
    # response = requests.get(url="https://api.sunrise-sunset.org/json")
    response.raise_for_status() 
    
    data = response.json()
    
    # pulling sunrise and sunset out of json data:
    sunrise_whole = data['results']['sunrise']
    print(sunrise_whole)
    sunset_whole = data['results']['sunset']
    print(sunset_whole)

    sunrise = int(data['results']['sunrise'].split(":")[0]),data['results']['sunrise'].split(" ")[1]
    sunset = int(data['results']['sunset'].split(":")[0]), data['results']['sunset'].split(" ")[1]
    
    print(f"For these coordinates, the sunrise time is: {sunrise} and the sunset time is {sunset}.")

    # current time:
    time_now = datetime.now()
    print(time_now.hour)

    # response_code
    print(response.status_code)
    return print(data['status'])
get_sunrise_sunset()