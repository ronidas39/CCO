import os
import requests
from fastapi import FastAPI, HTTPException, Query
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Google Search API Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CX_ID = os.getenv("GOOGLE_CX_ID")
SEARCH_URL = "https://www.googleapis.com/customsearch/v1"

@app.get("/search")
async def search_google(query: str, num_results: int = 10, page: int = 1):
    """Fetch Google search results using Custom Search API with pagination support"""
    start_index = (page - 1) * num_results + 1  # Calculate the start index for pagination

    params = {
        "key": GOOGLE_API_KEY,
        "cx": GOOGLE_CX_ID,
        "q": query,
        "num": num_results,
        "start": start_index
    }
    response = requests.get(SEARCH_URL, params=params)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch search results")
    
    results = response.json().get("items", [])
    return {
        "query": query,
        "page": page,
        "num_results": num_results,
        "results": [
            {
                "title": item["title"],
                "link": item["link"],
                "snippet": item.get("snippet", "")
            }
            for item in results
        ]
    }
