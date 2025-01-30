from fastapi import FastAPI, HTTPException
from openai import OpenAI
import os

app = FastAPI()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Set API key as an environment variable

# Define the OpenAI function for intent analysis
tools = [{
    "type": "function",
    "function": {
        "name": "analyze_intent",
        "description": "Analyzes user input and extracts intent.",
        "parameters": {
            "type": "object",
            "properties": {
                "intent": {
                    "type": "string",
                    "description": "The intent of the user's message (e.g., 'research','content generation','ad template copy','post content','invalid')."
                },
                "confidence": {
                    "type": "number",
                    "description": "Confidence score of the intent detection (0-1)."
                }
            },
            "required": ["intent", "confidence"],
            "additionalProperties": False
        },
        "strict": True
    }
}]

@app.get("/")
def home():
    return {"message": "FastAPI OpenAI Intent Analysis"}

@app.post("/analyze_intent/")
def analyze_intent(user_input: str):
    """
    Calls OpenAI API to analyze user input and detect intent.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": user_input}],
            tools=tools
        )

        tool_calls = response.choices[0].message.tool_calls
        return {"intent_analysis": tool_calls}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
