import os
import requests
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Flodesk API Configuration
BASE_URL = "https://api.flodesk.com/v1"
API_KEY = os.getenv("FLODESK_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

@app.post("/subscribers")
async def create_or_update_subscriber(email: str, first_name: str = None, last_name: str = None, custom_fields: dict = None):
    """Create or update a subscriber in Flodesk."""
    url = f"{BASE_URL}/subscribers"
    payload = {
        "email": email,
        "firstName": first_name,
        "lastName": last_name,
        "customFields": custom_fields or {}
    }
    response = requests.post(url, json=payload, headers=HEADERS)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@app.get("/subscribers/{subscriber_id}")
async def get_subscriber(subscriber_id: str):
    """Retrieve a subscriber by ID."""
    url = f"{BASE_URL}/subscribers/{subscriber_id}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@app.get("/segments")
async def list_segments():
    """List all segments."""
    url = f"{BASE_URL}/segments"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@app.post("/subscribers/{subscriber_id}/segments")
async def add_subscriber_to_segments(subscriber_id: str, segment_ids: list):
    """Add a subscriber to one or more segments."""
    url = f"{BASE_URL}/subscribers/{subscriber_id}/segments"
    payload = {"segment_ids": segment_ids}
    response = requests.post(url, json=payload, headers=HEADERS)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@app.post("/webhooks")
async def create_webhook(url: str, events: list):
    """Create a webhook to receive event notifications."""
    endpoint = f"{BASE_URL}/webhooks"
    payload = {
        "url": url,
        "events": events
    }
    response = requests.post(endpoint, json=payload, headers=HEADERS)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()
