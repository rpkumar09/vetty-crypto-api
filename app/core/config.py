from pydantic_settings import BaseSettings
from pydantic import AnyUrl
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    # Application Configuration
    PROJECT_NAME: str = "Vetty Crypto API"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")  # production/staging
    
    # Security Configuration
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # API Configuration
    COINGECKO_API_URL: AnyUrl = os.getenv("COINGECKO_API_URL", "https://api.coingecko.com/api/v3")
    
    # Pagination Defaults
    DEFAULT_PAGE_SIZE: int = 10
    MAX_PAGE_SIZE: int = 100
    
    class Config:
        case_sensitive = True

settings = Settings()