import os

class AppConfig:
    APP_NAME = "Messaging Service"  # Название приложения
    APP_VERSION = "1.0.0"  # Версия приложения
    HOST = "0.0.0.0"
    PORT = 8000
    LOG_LEVEL = "info"

class DatabaseConfig:
    DATABASE_URL = (
        f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
        f"@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
    )
