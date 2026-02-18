import requests

API_URL = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url=API_URL)

for key, value in response.json().items():
    if key == "userId":
        if value in [1, 2, 3]:
            print("User Found")
        else:
            print("User not found")
