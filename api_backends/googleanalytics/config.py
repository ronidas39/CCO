import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GA_PROPERTY_ID = os.getenv("GA_PROPERTY_ID")
