import csv
import requests
import os

# Allow override via ENV or fallback to localhost
API_URL = os.getenv("API_URL", "http://localhost:8000/trigger")

def onboard_users_from_csv(csv_path="users.csv"):
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            payload = {
                "action": "onboard",
                "displayName": row["displayName"],
                "nickname": row["nickname"],
                "upn": row["upn"],
                "password": row["password"]
            }
            print(f"⏳ Creating user: {row['upn']}")
            try:
                response = requests.post(API_URL, json=payload)
                print(f"✅ Status {response.status_code}: {response.json()}")
            except requests.exceptions.RequestException as e:
                print(f"❌ Failed to create user {row['upn']}: {e}")

if __name__ == "__main__":
    onboard_users_from_csv()
