# AI Agent for IAM (Microsoft Entra ID)

This is a Python-based FastAPI service to automate user onboarding and offboarding in Microsoft Entra ID using Graph API.

## Endpoints

### POST /trigger

**Payload for onboarding:**
```json
{
  "action": "onboard",
  "displayName": "Aditi Sharma",
  "nickname": "aditisharma",
  "upn": "aditisharma@idenaccess.onmicrosoft.com",
  "password": "Welcome@123"
}
```

**Payload for offboarding:**
```json
{
  "action": "offboard",
  "user_id": "aditisharma@idenaccess.onmicrosoft.com"
}
```

## Setup

1. Add your Microsoft Entra credentials to `utils.py`.
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `uvicorn main:app --reload`
