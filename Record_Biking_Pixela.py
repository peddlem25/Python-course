# using pixela https://pixe.la

import requests 
from datetime import datetime

USERNAME = "peddlem007"
TOKEN = "kuzcekxixbyh"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users" 

user_params = {
    "token": TOKEN, 
    "username": USERNAME, 
    "agreeTermsOfService":"yes", 
    "notMinor":"yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {
    "id": GRAPH_ID, 
    "name": "Biking Goals", 
    "unit":"km", 
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Test to see it works
# https://pixe.la/v1/users/peddlem007/graphs/graph1.html

# Create event
event_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# today = today.strftime("%Y%m%")

# 2021-06-12 16:09:16.472054 
# convert to yyyyMMdd

# becuase the requested dated is Str we need to add "" for the date and quantity.
pixel_data = {
    "date": today.strftime("%Y%m%"),
    "quantity": input("How many kms did you bike today? "),
}

# response = requests.post(url=event_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# Edit/ Update event PUT

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(requests.text)
