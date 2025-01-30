from fastapi import FastAPI, HTTPException
from transformers import pipeline

app = FastAPI()

# Load a Hugging Face model for intent classification
classifier = pipeline("text-classification", model="facebook/bart-large-mnli")  # Example model

@app.get("/")
def home():
    return {"message": "Hugging Face Intent Detection API"}

@app.post("/analyze_intent/local")
def analyze_intent(user_input: str):
    """
    Uses Hugging Face's Transformers API to analyze user input and determine intent.
    """
    try:
        result = classifier(user_input)
        intent = result[0]["label"]  # Extract predicted label
        confidence = result[0]["score"]  # Extract confidence score

        return {"intent": intent, "confidence": confidence}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
import requests
from fastapi import FastAPI, HTTPException
import os

app = FastAPI()

# Set your Hugging Face API key
HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")  # Store it as an environment variable

# Hugging Face Inference API URL
HF_API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"

# Headers with Authorization
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

@app.get("/")
def home():
    return {"message": "Hugging Face API Intent Detection"}

@app.post("/analyze_intent/")
def analyze_intent(user_input: str):
    """
    Calls Hugging Face's hosted Inference API to analyze intent.
    """
    try:
        response = requests.post(HF_API_URL, headers=HEADERS, json={"inputs": user_input})

        if response.status_code == 200:
            result = response.json()
            intent = result[0]["label"]
            confidence = result[0]["score"]
            return {"intent": intent, "confidence": confidence}
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

