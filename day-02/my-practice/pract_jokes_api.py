import requests

api_url = "http://www.official-joke-api.appspot.com/random_joke" # Step 1 API
dad_joke_url = "https://icanhazdadjoke.com/"

def get_joke(url_type,mood):
    headers = {
        "Accept": "application/json"
    }
    response = requests.get(url=url_type,headers=headers) # Step-2: Interacting with API
    if mood == "Dad":
        final_joke = response.json()["joke"]
    if mood == "PJ":
        final_joke = response.json()["setup"] + response.json()["punchline"] # Step-3: Collecting the responses which is necessary
    return final_joke # Step-4: Returning the output

mood  = input("Which joke would you like to hear? eg. (Dad, PJ)")
if mood == "Dad":
    url_type = dad_joke_url
elif mood == "PJ":
    url_type = api_url
else:
    url_type = dad_joke_url

final_joke = get_joke(url_type,mood) #Step-5: Grabing the modified request

print(final_joke) # Final Step: Printing the final joke
