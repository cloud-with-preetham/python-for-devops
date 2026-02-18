import requests
import json
from requests.exceptions import RequestException

API_URL = "https://jsonplaceholder.typicode.com/users"
OUTPUT_FILE = "output.json"


def fetch_user():
    try:
        response = requests.get(url=API_URL, timeout=5)
        response.raise_for_status()
        return response.json()

    except RequestException as error:
        print(f"Error fetching data from API {error}")


def process_users(users):
    processed_data = []

    if not users:
        print("No user data found")
        return processed_data

    for user in users:
        try:
            processed_data.append(
                {
                    "id": user.get("id"),
                    "name": user.get("name"),
                    "email": user.get("email"),
                    "address": user.get("address", {}).get("city"),
                    "phone": user.get("phone"),
                    "website": user.get("website"),
                }
            )
        except (KeyError, TypeError) as error:
            print(f"Skipping due to data error {error}")
    return processed_data


def save_to_output(data, filename):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Data successfully saved to {filename}")

    except IOError as error:
        print(f"Error writing in file {error}")


def main():
    print("Fetching user data")
    users = fetch_user()

    if not users:
        print("Exiting program due to API failure")
        return

    print("Processing data")
    processed_user = process_users(users)

    print("\nProcessing Output")
    for user in processed_user:
        print(user)

    print(f"Saving data to the {OUTPUT_FILE}....")
    save_to_output(processed_user, OUTPUT_FILE)

    print("Task Completed...!")


if __name__ == "__main__":
    main()
