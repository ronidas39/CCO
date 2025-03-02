# flodesk.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

app = FastAPI()

class FlodeskLogin(BaseModel):
    login_url: str  # URL of the Flodesk login page, e.g., "https://app.flodesk.com/login"
    email: str
    password: str

@app.post("/flodesk_login")
def flodesk_login(credentials: FlodeskLogin):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    except Exception:
        raise HTTPException(status_code=500, detail="Error initializing the web driver.")
    
    try:
        # Open the Flodesk login page
        driver.get(credentials.login_url)
        time.sleep(5)  # Wait for the page to load

        # Locate the email input field and enter the email
        email_field = driver.find_element(By.XPATH, "//input[@name='email']")
        email_field.send_keys(credentials.email)
        time.sleep(1)
        
        # Locate the password input field and enter the password
        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys(credentials.password)
        time.sleep(1)
        
        # Click the login button (adjust the XPath if needed)
        login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Log In')]")
        login_button.click()
        time.sleep(5)
        
        # Optionally, you can add logic here to verify successful login (e.g., checking for a dashboard element)
        return {"message": "Flodesk login successful!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        driver.quit()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)
