import os
import requests
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Instagram Ads API Configuration
GRAPH_API_VERSION = "v18.0"
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
AD_ACCOUNT_ID = os.getenv("AD_ACCOUNT_ID")
INSTAGRAM_ACCOUNT_ID = os.getenv("INSTAGRAM_ACCOUNT_ID")
API_URL = f"https://graph.facebook.com/{GRAPH_API_VERSION}/"

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

@app.post("/create-ad-creative")
async def create_ad_creative(image_url: str, caption: str):
    """Create an Instagram Ad Creative"""
    url = f"{API_URL}{AD_ACCOUNT_ID}/adcreatives"
    payload = {
        "name": "Instagram Ad Creative",
        "object_story_spec": {
            "instagram_actor_id": INSTAGRAM_ACCOUNT_ID,
            "link_data": {
                "image_url": image_url,
                "message": caption,
            }
        },
        "access_token": ACCESS_TOKEN,
    }
    response = requests.post(url, json=payload)
    return response.json()

@app.post("/create-instagram-ad")
async def create_instagram_ad(adset_id: str, creative_id: str, start_time: int, end_time: int):
    """Create an Instagram Ad with scheduled start and end time"""
    url = f"{API_URL}{AD_ACCOUNT_ID}/ads"
    payload = {
        "name": "Instagram Scheduled Ad",
        "adset_id": adset_id,
        "creative": {"creative_id": creative_id},
        "status": "PAUSED",  # Can be set to "ACTIVE" when ready
        "start_time": start_time,  # Unix timestamp
        "end_time": end_time,  # Unix timestamp
        "access_token": ACCESS_TOKEN,
    }
    response = requests.post(url, json=payload)
    return response.json()

@app.get("/ads-insights")
async def get_ads_insights(ad_id: str):
    """Track ad performance using insights"""
    url = f"{API_URL}{ad_id}/insights"
    params = {
        "fields": "impressions,clicks,spend,ctr,cpc",
        "access_token": ACCESS_TOKEN,
    }
    response = requests.get(url, params=params)
    return response.json()

@app.post("/update-ad-budget")
async def update_ad_budget(adset_id: str, new_budget: int):
    """Automate budget adjustment for better performance"""
    url = f"{API_URL}{adset_id}"
    payload = {
        "daily_budget": new_budget,
        "access_token": ACCESS_TOKEN,
    }
    response = requests.post(url, json=payload)
    return response.json()
