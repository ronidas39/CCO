import os
import requests
from fastapi import FastAPI, HTTPException, Query
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Google Analytics API Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GA_PROPERTY_ID = os.getenv("GA_PROPERTY_ID")
ANALYTICS_URL = "https://analyticsdata.googleapis.com/v1beta/properties"

@app.get("/analytics/report")
async def get_analytics_report(metric: str = "sessions", dimension: str = "date", start_date: str = "7daysAgo", end_date: str = "today"):
    """Fetch Google Analytics report data"""
    url = f"{ANALYTICS_URL}/{GA_PROPERTY_ID}:runReport"
    headers = {"Authorization": f"Bearer {GOOGLE_API_KEY}"}
    payload = {
        "dateRanges": [{"startDate": start_date, "endDate": end_date}],
        "metrics": [{"name": metric}],
        "dimensions": [{"name": dimension}]
    }
    
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch analytics data")
    
    return response.json()
