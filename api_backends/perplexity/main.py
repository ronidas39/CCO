import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

app = FastAPI()

PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
PERPLEXITY_API_URL = "https://api.perplexity.ai/chat/completions"

class Message(BaseModel):
    role: str
    content: str

class QueryRequest(BaseModel):
    model: str
    messages: list[Message]
    max_tokens: int = 100
    temperature: float = 0.7

@app.post("/query")
async def query_perplexity(request: QueryRequest):
    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    response = requests.post(PERPLEXITY_API_URL, headers=headers, json=request.dict())
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch response from Perplexity API")
    return response.json()
