import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SPRING_BOOT_URL = os.getenv("SPRING_BOOT_URL", "http://localhost:8080")
    PORT = int(os.getenv("PORT", 8000))