import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "mrdkyl"
TOKEN = "j45n6kl4hgl546hdg4"

pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(pixela_endpoint, json=pixela_params)
# print(response.text)

# ----------------- Creating the coding graph -----------------
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "coding-graph",
    "name": "Coding Graph",
    "unit": "hour",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
#
# link_of_graph = "https://pixe.la/v1/users/mrdkyl/graphs/coding-graph.html"
# ----------------------------------------------------------------------


# ----------------- Posting pixels to our Coding Graph -----------------
today = datetime.now()
print(today)
date = today.strftime("%Y%m%d")
print(date)

post_pixel_params = {
    "date": "20220418",
    "quantity": str(input("How many hours did you write code today?"))
}

post_pixel_endpoint = f"{graph_endpoint}/{graph_params['id']}"

# response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=headers)
# print(response.text)
# ---------------------------------------------------------------------------------------------------------------------

# ----------------- Putting different value to the pixel which is already created in our Coding Graph -----------------
put_endpoint = f"{post_pixel_endpoint}/20220418"

put_params = {
    "quantity": "6.2"
}

# response = requests.put(url=put_endpoint, json=put_params, headers=headers)
# print(response.text)
# -------------------------------------------------------------

# ----------------- Deleting pixel from Graph -----------------
delete_endpoint = put_endpoint
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
