api_keys = "22955db72cbbf3a4ef8f4c74a7f0bba7"
import requests

parameter = {

    "lat": 42.698334,
    "lon": 23.319941,
    "appid": api_keys
}

r = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=parameter)

out = r.json()

list1 = (out["list"][x]["weather"] for x in range(len(out["list"])) if x < 10)

list_id = [y[0]["id"] for y in list1 if y[0]["id"] < 700]

if len(list_id) > 0:
    print("take the umbrella")
print(list_id)
