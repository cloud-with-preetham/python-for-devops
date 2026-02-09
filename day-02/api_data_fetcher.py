#!/usr/bin/env python3

import requests
import json

API_URL = "https://jsonplaceholder.typicode.com/users"
OUTPUT_FILE = "output.json"

def fetch_user():# -> Any:
    """I am fetching the user data from public API"""
    response = requests.get(API_URL)
    response.raise_for_status() # Raises errors if API calls fails.
    return response.json()

def process_users(users): # -> list[Any]:
    """I am scraping/extracting meaningful information from API response"""
    processed_data = []

    for user in users:
        processed_data.append({
            "id": user["id"],
            "name": user["name"],
            "username": user["username"],
            "email": user["email"],
            "city": user["address"]["city"],
            "company": user["company"]["name"]        
        })
    return processed_data

def save_to_json(data,filename) -> None:
    """I am saving the processed data to JSON file"""
    with open(filename, "w") as f:
        json.dump(data,f,indent=1)

def main():
    print("Fetching data from API")
    users = fetch_user()

    print("Processing Data....")
    processed_users = process_users(users)

    print("\nProcessed Output")
    for user in processed_users:
        print(user)

    print(f"\nSaving data to {OUTPUT_FILE}....")
    save_to_json(processed_users,OUTPUT_FILE)

    print("Task Accomplished")

if __name__ == "__main__":
    main()
