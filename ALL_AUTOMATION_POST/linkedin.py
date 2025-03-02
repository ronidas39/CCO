from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load environment variables (ensure you have a .env file with your credentials)
load_dotenv()

app = FastAPI()

class PostRequest(BaseModel):
    topic: str

def post_to_linkedin(topic: str):
    # LinkedIn credentials and post content
    USERNAME = os.getenv("user")
    PASSWORD = os.getenv("pwd")
    POST_CONTENT = topic

    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        # Open LinkedIn login page
        driver.get("https://www.linkedin.com/login")
        
        # Wait for the username field to load, then input username
        wait = WebDriverWait(driver, 10)
        username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        username_field.send_keys(USERNAME)
        
        # Input password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.RETURN)
        
        # Wait until home page is loaded (check for the search bar as an indicator)
        wait.until(EC.presence_of_element_located((By.ID, "global-nav-search")))
        time.sleep(3)  # Additional wait to ensure the page fully loads
        
        # Click on the "Start a post" button (the class name may change over time)
        start_post_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "share-box-feed-entry__closed-share-box")))
        start_post_button.click()
        
        # Wait for the post modal to appear and find the text area
        text_area = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-placeholder='What do you want to talk about?']")))
        text_area.click()
        text_area.send_keys(POST_CONTENT)
        
        # Wait for the "Post" button to be clickable and click it
        post_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'share-actions__primary-action')]")))
        post_button.click()
        
        # Optional: Wait a few seconds to ensure the post is submitted
        time.sleep(5)
    finally:
        # Close the browser
        driver.quit()

@app.post("/post")
def create_post(request: PostRequest):
    try:
        post_to_linkedin(request.topic)
        return {"message": "Post created successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
