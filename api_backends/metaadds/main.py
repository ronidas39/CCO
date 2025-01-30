import os
import requests
from fastapi import FastAPI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Meta API Configuration
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
AD_ACCOUNT_ID = os.getenv("AD_ACCOUNT_ID")
GRAPH_API_VERSION = "v18.0"
API_URL = f"https://graph.facebook.com/{GRAPH_API_VERSION}/act_{AD_ACCOUNT_ID}"

@app.post("/create-campaign")
async def create_campaign(name: str, objective: str = "LINK_CLICKS", status: str = "PAUSED"):
    """Create a new campaign in Meta Ads"""
    url = f"{API_URL}/campaigns"
    payload = {
        "name": name,
        "objective": objective,
        "status": status,
        "buying_type": "AUCTION",
        "special_ad_categories": [],
        "access_token": ACCESS_TOKEN,
    }
    response = requests.post(url, json=payload)
    return response.json()

@app.post("/create-adset")
async def create_adset(name: str, campaign_id: str, daily_budget: int, targeting: dict):
    """Create an ad set inside a campaign"""
    url = f"{API_URL}/adsets"
    payload = {
        "name": name,
        "campaign_id": campaign_id,
        "daily_budget": daily_budget,
        "billing_event": "IMPRESSIONS",
        "optimization_goal": "REACH",
        "targeting": targeting,
        "status": "PAUSED",
        "access_token": ACCESS_TOKEN,
    }
    response = requests.post(url, json=payload)
    return response.json()

@app.post("/create-ad")
async def create_ad(name: str, adset_id: str, creative_id: str):
    """Create an ad inside an ad set"""
    url = f"{API_URL}/ads"
    payload = {
        "name": name,
        "adset_id": adset_id,
        "creative": {"creative_id": creative_id},
        "status": "PAUSED",
        "access_token": ACCESS_TOKEN,
    }
    response = requests.post(url, json=payload)
    return response.json()

@app.get("/get-campaigns")
async def get_campaigns():
    """Fetch all campaigns from Meta Ads"""
    url = f"{API_URL}/campaigns"
    params = {
        "fields": "id,name,status,objective",
        "access_token": ACCESS_TOKEN,
    }
    response = requests.get(url, params=params)
    return response.json()

@app.get("/get-adsets")
async def get_adsets():
    """Fetch all ad sets from Meta Ads"""
    url = f"{API_URL}/adsets"
    params = {
        "fields": "id,name,status,campaign_id,daily_budget,targeting",
        "access_token": ACCESS_TOKEN,
    }
    response = requests.get(url, params=params)
    return response.json()

@app.get("/get-ads")
async def get_ads():
    """Fetch all ads from Meta Ads"""
    url = f"{API_URL}/ads"
    params = {
        "fields": "id,name,status,adset_id,creative",
        "access_token": ACCESS_TOKEN,
    }
    response = requests.get(url, params=params)
    return response.json()
@app.post("/create-adcreative")
async def create_ad_creative(name: str, page_id: str, link: str, message: str):
    """Create an Ad Creative and return creative_id"""
    url = f"{API_URL}/adcreatives"
    payload = {
        "name": name,
        "object_story_spec": {
            "page_id": page_id,
            "link_data": {
                "link": link,
                "message": message,
            },
        },
        "access_token": ACCESS_TOKEN,
    }
    response = requests.post(url, json=payload)
    return response.json()
