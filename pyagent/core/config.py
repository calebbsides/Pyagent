import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    BASE_MODEL: str = os.getenv("BASE_MODEL", "gemini-2.5-flash")

settings = Settings()
