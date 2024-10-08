import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    
    DATABASE_URL: str = "postgresql://user:password@localhost/dbname"

    # Налаштування для аутентифікації
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your_secret_key")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Налаштування логування
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    class Config:
        # Дозволити читання з файлу .env
        env_file = ".env"
        env_file_encoding = 'utf-8'


# Ініціалізація налаштувань
settings = Settings()
