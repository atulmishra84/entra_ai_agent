import requests

def get_token():
    tenant_id = "71ee5ddd-1b7c-436d-acb1-0b260b2b2061"
    client_id = "2df0e631-1e05-45df-8b2d-a2c99e5ba013"
    client_secret = "6ax8Q~ZWFVD~n6ZZAL6kirPktcyWpESQCzHbYbMm"
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "https://graph.microsoft.com/.default",
        "grant_type": "client_credentials"
    }

    response = requests.post(url, data=payload)

    if response.status_code != 200:
        raise Exception(f"Failed to get token: {response.status_code} {response.text}")

    return response.json().get("access_token")
