import requests
from datetime import datetime

url = "https://api.sunrise-sunset.org/json"

parameters = {"lat": "29.62217", "lng": "52.54688", "date": "today"}
r = requests.get(url, parameters)
# print(r.status_code)


# time_str = "13::55::26"
# time_object = datetime.strptime(time_str, "%H::%M::%S").time()

data = r.json()

time_object = datetime.strptime(data["results"]["sunrise"].split()[0], "%H:%M:%S")
delta_time = datetime.strptime("02:30:00", "%H:%M:%S")
time_zero = datetime.strptime("00:00:00", "%H:%M:%S")
sunrise = time_object - time_zero + delta_time

# print("sunrise:", data["results"]["sunrise"])
print("sunrise:", sunrise)
print("sunset:", data["results"]["sunset"])
