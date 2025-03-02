# calendly.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

app = FastAPI()

class CalendlyBooking(BaseModel):
    booking_url: str  # e.g., "https://calendly.com/username/meeting-type"
    name: str
    email: str
    phone: str = None  # Optional phone number
    note: str = None   # Optional note or message

@app.post("/calendly_booking")
def book_calendly_event(booking: CalendlyBooking):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    except Exception:
        raise HTTPException(status_code=500, detail="Error initializing the web driver.")
    
    try:
        # Open the Calendly booking page
        driver.get(booking.booking_url)
        time.sleep(5)  # Allow time for the page to load

        # Select a time slot
        # The XPath below is generic; adjust it as needed based on your page's structure.
        timeslot = driver.find_element(By.XPATH, "//button[contains(text(),'Select')]")
        timeslot.click()
        time.sleep(3)

        # Fill out the booking form

        # Enter the name
        name_field = driver.find_element(By.XPATH, "//input[@name='name']")
        name_field.send_keys(booking.name)
        time.sleep(1)
        
        # Enter the email address
        email_field = driver.find_element(By.XPATH, "//input[@name='email']")
        email_field.send_keys(booking.email)
        time.sleep(1)
        
        # Optionally enter the phone number if provided
        if booking.phone:
            phone_field = driver.find_element(By.XPATH, "//input[@name='phone']")
            phone_field.send_keys(booking.phone)
            time.sleep(1)
        
        # Optionally enter a note if provided
        if booking.note:
            note_field = driver.find_element(By.XPATH, "//textarea[@name='note']")
            note_field.send_keys(booking.note)
            time.sleep(1)
        
        # Confirm the booking
        # The XPath below assumes the button text includes
