import requests
from dotenv import load_dotenv
import os
import time

load_dotenv()

# myuser
# https://pixe.la/@vladimirb

# 1.Create User
PIXELA_URL = os.getenv('PIXELA_URL')


user_params = {
    "token": os.getenv('TOKEN'),
    "username": "vladimirb",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url = PIXELA_URL, json = user_params)
# print(response.text)

#2.Create a graph definition
USERNAME = os.getenv('USERNAME')
GRAPH_ENDPOINT = f"{PIXELA_URL}/{USERNAME}/graphs"
print(GRAPH_ENDPOINT)

graph_params = {
    "id": os.getenv('GRAPH_ID'),
    "name": "Learning Graph",
    "unit": "hours",
    "type": "int",
    "color": "sora"
}

token_headers = {
    "X-USER-TOKEN": os.getenv('TOKEN')
}

response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=token_headers)
# print(response.text)

#3.Post to graph
# https://pixe.la/v1/users/vladimirb/graphs/graph1.html

VALUE_GRAPH_URL = f"{PIXELA_URL}/{USERNAME}/graphs/{os.getenv('GRAPH_ID')}"
time.strftime("%Y%m%d")
graph_value_params = {
    "date": time.strftime("%Y%m%d"),
    "quantity": "10"
}

response = requests.post(url=VALUE_GRAPH_URL, json=graph_value_params, headers=token_headers)
print(response.text)
