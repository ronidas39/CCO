# thread.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

app = FastAPI()

class ThreadsPost(BaseModel):
    username: str
    password: str
    post_content: str

@app.post("/threads_post")
def create_threads_post(post: ThreadsPost):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    except Exception:
        raise HTTPException(status_code=500, detail="Error initializing the web driver.")
    
    try:
        # Navigate to Threads (assumes threads.net)
        driver.get("https://www.threads.net/")
        time.sleep(5)
        
        # Click on "Log in with Instagram" button
        login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Log in with Instagram')]")
        login_button.click()
        time.sleep(5)
        
        # Log in using Instagram credentials
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        username_field.send_keys(post.username)
        password_field.send_keys(post.password)
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)
        
        # Optionally dismiss any pop-ups
        try:
            dismiss = driver.find_element(By.XPATH, "//button[contains(text(),'Not Now')]")
            dismiss.click()
            time.sleep(3)
        except:
            pass
        
        # Locate the post creation box and enter text
        post_box = driver.find_element(By.XPATH, "//textarea[@placeholder=\"What's happening?\"]")
        post_box.click()
        time.sleep(2)
        post_box.send_keys(post.post_content)
        time.sleep(2)
        
        # Click the "Post" button
        post_button = driver.find_element(By.XPATH, "//button[contains(text(),'Post')]")
        post_button.click()
        time.sleep(5)
        
        return {"message": "Threads post published successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        driver.quit()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
