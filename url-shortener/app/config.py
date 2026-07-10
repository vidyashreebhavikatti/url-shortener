import os
from dotenv import load_dotenv

#load variables from .env
load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME", "URL Shortener")
    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
    DEBUG = os.getenv("DEBUG", "False") == "True"
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/url_shortener")

settings = Settings()




