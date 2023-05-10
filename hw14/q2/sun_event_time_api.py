import requests
import datetime


def get_exact_time_for_iran(api_time):  # add 2:30 to time recieved
    time_object = datetime.datetime.strptime(api_time, "%H:%M:%S")
    delta_time = datetime.timedelta(minutes=30, hours=2)
    return time_object + delta_time


url = "https://api.sunrise-sunset.org/json"

parameters = {"lat": "29.62217", "lng": "52.54688", "date": "today"}
r = requests.get(url, parameters)
# print(r.status_code)

data = r.json()

sunrise_time = get_exact_time_for_iran(data["results"]["sunrise"].split()[0])
sunset_time = get_exact_time_for_iran(data["results"]["sunset"].split()[0])

print(f"sunrise:{sunrise_time}")
print(f"sunset:{sunset_time}")
