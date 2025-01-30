import os
import requests
from fastapi import FastAPI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Calendly API Configuration
BASE_URL = "https://api.calendly.com"
ACCESS_TOKEN = os.getenv("CALENDLY_ACCESS_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

@app.get("/user-info")
async def get_user_info():
    """Get the current authenticated user's information"""
    url = f"{BASE_URL}/users/me"
    response = requests.get(url, headers=HEADERS)
    return response.json()

@app.get("/event-types")
async def get_event_types():
    """Get available event types for the user"""
    url = f"{BASE_URL}/event_types"
    response = requests.get(url, headers=HEADERS)
    return response.json()

@app.get("/scheduled-events")
async def get_scheduled_events():
    """Retrieve all scheduled events"""
    url = f"{BASE_URL}/scheduled_events"
    response = requests.get(url, headers=HEADERS)
    return response.json()

@app.post("/create-webhook")
async def create_webhook(url: str, events: list):
    """Create a webhook for event notifications"""
    payload = {
        "url": url,
        "events": events
    }
    url = f"{BASE_URL}/webhooks"
    response = requests.post(url, json=payload, headers=HEADERS)
    return response.json()
