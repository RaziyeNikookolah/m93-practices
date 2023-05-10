import requests

url = "https://api.sunrise-sunset.org/json?lat=29.62217&lng=52.54688&&date=2023-05-10"



r = requests.get(url)  
# print(r.status_code)

data = r.json()
print("sunrise:", data["results"]["sunrise"])
print("sunset:", data["results"]["sunset"])