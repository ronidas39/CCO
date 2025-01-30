from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import requests
import requests
import os
from dotenv import load_dotenv
load_dotenv()
app = FastAPI()

# Replace these with your LinkedIn app's credentials
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = "https://www.linkedin.com/developers/tools/oauth/redirect"
AUTH_URL = "https://www.linkedin.com/oauth/v2/authorization"
TOKEN_URL = "https://www.linkedin.com/oauth/v2/accessToken"
POST_URL = "https://api.linkedin.com/v2/ugcPosts"
ACCESS_TOKEN = os.getenv("ACCES_TOKEN")
POST_URL = "https://api.linkedin.com/v2/ugcPosts"
token=""



def auth():
# Replace with your actual LinkedIn access token

    # LinkedIn API endpoint to fetch user information
    USER_INFO_URL = "https://api.linkedin.com/v2/userinfo"

    # Set up headers
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    # Make the GET request
    response = requests.get(USER_INFO_URL, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        user_info = response.json()
        token=user_info["sub"]
        return token
    else:
        print("Error fetching user info:", response.status_code, response.text)


@app.post("/post")
def create_linkedin_post():
    token=auth()
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }
    post_data = {
        "author": f"urn:li:person:{token}",  # Replace with actual user URN
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": "posting from api"
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    response = requests.post(POST_URL, headers=headers, json=post_data)

    if response.status_code == 201:
        return {"message": "Post created successfully!", "response": response.json()}
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)






