import requests
import json

API_URL = "https://jsonplaceholder.typicode.com/users"
OUTPUT_FILE = "output.json"


def fetch_user():
    response = requests.get(url=API_URL)
    return response.json()


def process_users(users):
    processed_data = []

    for user in users:
        processed_data.append(
            {
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
                "address": user["address"]["city"],
                "phone": user["phone"],
                "website": user["website"],
            }
        )
    return processed_data


def save_to_output(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def main():
    print("Fetching user data")
    users = fetch_user()

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
