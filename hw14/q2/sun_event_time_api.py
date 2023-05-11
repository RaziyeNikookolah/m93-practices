import requests
import datetime


def get_local_time(api_time):  # add 3:30 to time
    time_object = datetime.datetime.strptime(api_time, "%I:%M:%S %p")
    delta_time = datetime.timedelta(minutes=30, hours=3)
    return (time_object + delta_time).time()
#date time can get timezone and 
# beautifull soup4 y import bs4 is usfull
#api of github 

url = "https://api.sunrise-sunset.org/json"
parameters = {
    "lat": "29.62217",
    "lng": "52.54688",
    "date": "today",
}
r = requests.get(url, parameters)
if r.status_code == 200:
    data = r.json()

    sunrise_time = get_local_time(data["results"]["sunrise"])
    sunset_time = get_local_time(data["results"]["sunset"])

    print(f"sunrise:{sunrise_time} and sunset:{sunset_time}")
else:
    print("Error ..")
