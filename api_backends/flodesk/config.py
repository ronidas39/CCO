import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

FLODESK_API_KEY = os.getenv("FLODESK_API_KEY")
