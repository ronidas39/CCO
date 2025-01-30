import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

CALENDLY_ACCESS_TOKEN = os.getenv("CALENDLY_ACCESS_TOKEN")
