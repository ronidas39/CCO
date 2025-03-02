from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

app = FastAPI()

# Define the request model
class FacebookPost(BaseModel):
    username: str
    password: str
    post_content: str

@app.post("/facebook_post")
def create_facebook_post(post: FacebookPost):
    # Initialize WebDriver options
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")         # Maximized window
    options.add_argument("--disable-notifications")     # Disable notifications

    # Set up Chrome WebDriver
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error initializing the web driver.")

    try:
        # Open Facebook login page
        driver.get("https://www.facebook.com/")
        time.sleep(3)

        # Input email/phone
        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys(post.username)

        # Input password
        password_field = driver.find_element(By.ID, "pass")
        password_field.send_keys(post.password)
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)

        # Check for login failure by URL
        if "login" in driver.current_url:
            return {"error": "Login failed. Check your credentials."}
        else:
            # Navigate to homepage and wait for elements to load
            driver.get("https://www.facebook.com/")
            time.sleep(5)

            # Click on the "Create Post" section
            post_box = driver.find_element(By.XPATH, "//div[@aria-label='Create a post']")
            post_box.click()
            time.sleep(3)

            # Enter the post content
            active_post_box = driver.find_element(By.XPATH, '//div[@aria-label="What\'s on your mind?"]')
            active_post_box.send_keys(post.post_content)
            time.sleep(3)

            # Click the "Post" button
            post_button = driver.find_element(By.XPATH, "//div[@aria-label='Post']")
            post_button.click()
            time.sleep(5)

            return {"message": "Post published successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        driver.quit()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
