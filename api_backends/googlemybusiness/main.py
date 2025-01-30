import os
import requests
from fastapi import FastAPI, HTTPException, Query
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Google My Business API Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GMB_ACCOUNT_ID = os.getenv("GMB_ACCOUNT_ID")
GMB_BASE_URL = "https://mybusiness.googleapis.com/v4"

@app.get("/business/info")
async def get_business_info():
    """Fetch Google My Business account info"""
    url = f"{GMB_BASE_URL}/accounts/{GMB_ACCOUNT_ID}"
    headers = {"Authorization": f"Bearer {GOOGLE_API_KEY}"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch business info")
    
    return response.json()

@app.get("/locations")
async def get_business_locations():
    """Retrieve all locations associated with the Google My Business account"""
    url = f"{GMB_BASE_URL}/accounts/{GMB_ACCOUNT_ID}/locations"
    headers = {"Authorization": f"Bearer {GOOGLE_API_KEY}"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch locations")
    
    return response.json()

@app.post("/posts")
async def create_google_post(summary: str, action_url: str):
    """Create a Google My Business Post"""
    url = f"{GMB_BASE_URL}/accounts/{GMB_ACCOUNT_ID}/localPosts"
    headers = {"Authorization": f"Bearer {GOOGLE_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "summary": summary,
        "callToAction": {
            "actionType": "LEARN_MORE",
            "url": action_url
        },
        "event": {}  # Optional event details
    }
    
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to create post")
    
    return response.json()
