# whatsapp.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

app = FastAPI()

class WhatsAppMessage(BaseModel):
    contact_name: str  # Name of the contact or group as seen on WhatsApp Web
    message: str

@app.post("/whatsapp_post")
def send_whatsapp_message(msg: WhatsAppMessage):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    except Exception:
        raise HTTPException(status_code=500, detail="Error initializing the web driver.")
    
    try:
        # Open WhatsApp Web (QR scanning required on first use)
        driver.get("https://web.whatsapp.com/")
        time.sleep(20)  # Increase if needed for QR code scanning
        
        # Search for the contact or group
        search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='3']")
        search_box.click()
        time.sleep(2)
        search_box.send_keys(msg.contact_name)
        time.sleep(3)
        
        # Click on the matching contact
        contact = driver.find_element(By.XPATH, f"//span[@title='{msg.contact_name}']")
        contact.click()
        time.sleep(3)
        
        # Locate the message input box, type the message, and send it
        message_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='10']")
        message_box.click()
        time.sleep(2)
        message_box.send_keys(msg.message)
        time.sleep(1)
        message_box.send_keys(Keys.RETURN)
        time.sleep(3)
        
        return {"message": "Message sent successfully on WhatsApp Web!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        driver.quit()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
