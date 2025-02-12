import os
from dotenv import load_dotenv

# Load environment variables from keys.env file
load_dotenv(dotenv_path='keys.env')

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "7a6238b17d83d8e4e92f1015e8c3cf0357a5296e33860495d56cd82c3e8e6a50 ")
    #DATA_FILE = 'data.json'  # Path to the JSON storage file