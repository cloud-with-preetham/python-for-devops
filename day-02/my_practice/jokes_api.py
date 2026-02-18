from wsgiref import headers
import requests

"""
As a devops engineer, you will have to navigate through multiple external endpoints, and you should know how to switch them with python.
"""
jokes_url = "https://official-joke-api.appspot.com/random_joke"
dad_jokes_url = "https://icanhazdadjoke.com/"


def get_joke(url_type, mood):
    headers = {"Accept": "application/json"}
    jokes = requests.get(url=url_type, headers=headers)
    if mood == "dad":
        final_joke = jokes.json()["joke"]
    if mood == "pj":
        final_joke = jokes.json()["setup"] + jokes.json()["punchline"]
    return final_joke


mood = input("Enter what type of joke you wanna hear...eg. 'dad', 'pj': ")
if mood == "dad":
    url_type = dad_jokes_url
elif mood == "pj":
    url_type = jokes_url
else:
    url_type = dad_jokes_url
final_joke = get_joke(url_type, mood)

print(final_joke)
