import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["longitude"]

iss_position = ("Current Location (Logitude, Latitude): ", longitude, latitude)
print(iss_position)
