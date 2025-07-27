from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import os

from agent_logic import onboard_user, offboard_user

app = FastAPI(title="Microsoft Entra AI Agent", version="1.0")

class UserAction(BaseModel):
    action: str
    displayName: str | None = None
    nickname: str | None = None
    upn: str | None = None
    password: str | None = None
    user_id: str | None = None

@app.get("/", response_class=HTMLResponse)
def root():
    with open("static/frontend.html", "r") as f:
        return f.read()

@app.post("/trigger")
async def trigger_agent(payload: UserAction):
    data = payload.dict()
    action = data.get("action")

    if action == "onboard":
        return await onboard_user(data)
    elif action == "offboard":
        return await offboard_user(data)
    else:
        return {"status": "error", "message": "Unknown action"}
