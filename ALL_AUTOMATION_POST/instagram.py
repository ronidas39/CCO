# instagram.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

app = FastAPI()

class InstagramPost(BaseModel):
    username: str
    password: str
    image_path: str  # Local file path to the image you want to upload
    caption: str

@app.post("/instagram_post")
def create_instagram_post(post: InstagramPost):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    except Exception:
        raise HTTPException(status_code=500, detail="Error initializing the web driver.")
    
    try:
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        
        # Log in to Instagram
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        username_field.send_keys(post.username)
        password_field.send_keys(post.password)
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)
        
        # Dismiss pop-ups if present
        for _ in range(2):
            try:
                not_now = driver.find_element(By.XPATH, "//button[contains(text(),'Not Now')]")
                not_now.click()
                time.sleep(3)
            except:
                break

        # Click the "New Post" icon (this XPath may need updating)
        new_post_button = driver.find_element(By.XPATH, "//div[@role='menuitem']//*[name()='svg' and @aria-label='New Post']")
        new_post_button.click()
        time.sleep(3)
        
        # Upload the image file
        upload_input = driver.find_element(By.XPATH, "//input[@type='file']")
        upload_input.send_keys(post.image_path)
        time.sleep(5)
        
        # Click "Next"
        next_button = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
        next_button.click()
        time.sleep(3)
        
        # Enter the caption
        caption_area = driver.find_element(By.XPATH, "//textarea[@aria-label='Write a caption…']")
        caption_area.send_keys(post.caption)
        time.sleep(2)
        
        # Click "Share"
        share_button = driver.find_element(By.XPATH, "//button[contains(text(),'Share')]")
        share_button.click()
        time.sleep(5)

        return {"message": "Instagram post published successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        driver.quit()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
