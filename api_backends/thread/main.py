import os
import requests
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from urllib.parse import urlencode
import config

app = FastAPI()

GRAPH_API_BASE_URL = "https://graph.facebook.com/v18.0"

@app.get("/login")
async def login():
    """Initiate OAuth login for Threads API"""
    auth_url = (
        "https://www.facebook.com/v18.0/dialog/oauth?"
        + urlencode(
            {
                "client_id": config.CLIENT_ID,
                "redirect_uri": config.REDIRECT_URI,
                "scope": "threads_read,threads_write",
                "response_type": "code",
            }
        )
    )
    return RedirectResponse(auth_url)

@app.get("/callback")
async def callback(request: Request):
    """Handle OAuth callback and retrieve access token"""
    code = request.query_params.get("code")
    if not code:
        raise HTTPException(status_code=400, detail="Authorization code not found")

    token_url = f"{GRAPH_API_BASE_URL}/oauth/access_token"
    params = {
        "client_id": config.CLIENT_ID,
        "redirect_uri": config.REDIRECT_URI,
        "client_secret": config.CLIENT_SECRET,
        "code": code,
    }
    response = requests.get(token_url, params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch access token")

    tokens = response.json()
    access_token = tokens.get("access_token")
    if not access_token:
        raise HTTPException(status_code=400, detail="Access token not found")

    return {"access_token": access_token}

@app.post("/threads")
async def create_thread(message: str):
    """Create a new thread on Threads API"""
    url = f"{GRAPH_API_BASE_URL}/me/threads"
    headers = {"Authorization": f"Bearer {config.ACCESS_TOKEN}"}
    payload = {"message": message}

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to create thread")

    return response.json()
