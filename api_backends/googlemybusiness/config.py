import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GMB_ACCOUNT_ID = os.getenv("GMB_ACCOUNT_ID")
