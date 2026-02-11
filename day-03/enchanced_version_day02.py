#!/usr/bin/env python3

import requests
import json
from requests.exceptions import RequestException

API_URL = "https://jsonplaceholder.typicode.com/users"
OUTPUT_FILE = "output.json"

def fetch_user():
    """I am fetching the user data from public API"""
    try:
        response = requests.get(API_URL,timeout=5)
        response.raise_for_status() # Raises errors if API calls fails.
        return response.json()
    
    except RequestException as error:
        print(f"Error fetching data from API: {error}")

def process_users(users):
    """I am scraping/extracting meaningful information from API response"""
    processed_data = []

    if not users:
        print("No user data to process.")
        return processed_data

    for user in users:
        try:
            processed_data.append({
            "id": user.get("id"),
            "name": user.get("name"),
            "username": user.get("username"),
            "email": user.get("email"),
            "city": user.get("address",{}).get("city"),
            "company": user.get("company",{}).get("name")        
            })
        except (KeyError, TypeError) as error:
            print(f"Skipping user due to data error: {error}")
    return processed_data

def save_to_json(data,filename):
    """I am saving the processed data to JSON file"""
    try:
        with open(filename, "w") as f:
            json.dump(data,f,indent=4)
        print(f"Data successfully saved to {filename}")
    
    except IOError as error:
        print(f"Error writing in file: {error}")

def main():
    print("Fetching data from API")
    users = fetch_user()
    
    if not users:
        print("Exiting program due to API failure.")
        return
    
    print("Processing Data....")
    processed_users = process_users(users)

    print("\nProcessed Output")
    for user in processed_users:
        print(user)

    print(f"\nSaving data to {OUTPUT_FILE}....")
    save_to_json(processed_users,OUTPUT_FILE)

    print("Task Completed Successfully")

if __name__ == "__main__":
    main()
