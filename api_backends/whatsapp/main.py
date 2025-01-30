import os
import requests
from fastapi import FastAPI, Request
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Load config from environment
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

API_URL = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"

@app.post("/send-message/")
async def send_message(to: str, message: str):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": message}
    }
    
    response = requests.post(API_URL, json=payload, headers=headers)
    return response.json()

@app.get("/webhook")
async def verify_webhook(request: Request):
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")
    
    if mode == "subscribe" and token == VERIFY_TOKEN:
        return int(challenge)
    return {"error": "Invalid token"}

@app.post("/webhook")
async def handle_webhook(request: Request):
    data = await request.json()
    
    if "entry" in data:
        for entry in data["entry"]:
            for change in entry["changes"]:
                if "messages" in change["value"]:
                    for message in change["value"]["messages"]:
                        sender = message["from"]
                        text = message.get("text", {}).get("body", "No text")
                        print(f"Received message from {sender}: {text}")
    
    return {"status": "received"}
