import requests
import json
from utils import get_token

GRAPH_URL = "https://graph.microsoft.com/v1.0"

async def onboard_user(data):
    token = get_token()
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    user = {
        "accountEnabled": True,
        "displayName": data["displayName"],
        "mailNickname": data["nickname"],
        "userPrincipalName": data["upn"],
        "passwordProfile": {
            "forceChangePasswordNextSignIn": True,
            "password": data["password"]
        }
    }

    r = requests.post(f"{GRAPH_URL}/users", headers=headers, data=json.dumps(user))
    return r.json()

async def offboard_user(data):
    token = get_token()
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    user_id = data["user_id"]

    r = requests.patch(f"{GRAPH_URL}/users/{user_id}", headers=headers, json={"accountEnabled": False})
    return r.json()
