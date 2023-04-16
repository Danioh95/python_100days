import requests
from datetime import datetime

TOKEN = "fhja03fj0jf0akfja0jbx0xb9cb80x"
USERNAME = "danieleugo"
pixela_endpoint = "https://pixe.la/v1/users"

today_date = datetime.now()

user_params = {
    "token": "fhja03fj0jf0akfja0jbx0xb9cb80x",
    "username": "danieleugo",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Video",
    "type": "int",
    "color": "momiji"
}

graph_body = {
    "date": today_date.strftime("%Y%m%d"),
    "quantity": "7"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

print(today_date.strftime("%Y%m%d"))
response = requests.post(url=graph_endpoint, json=graph_body, headers=headers)
print(response.text)
