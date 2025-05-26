from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Access environment variables
nasa_api_key = os.getenv("NASA_API_KEY")
gee_email = os.getenv("GEE_USER_EMAIL")