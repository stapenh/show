from fastapi import FastAPI
from app.config import AppConfig
from app.endpoints import messaging
from database.database import init_db

app = FastAPI(title=AppConfig.APP_NAME, version=AppConfig.APP_VERSION)

# Подключаем роуты

app.include_router(messaging.router)

# Инициализируем базу данных при старте приложения
@app.on_event("startup")
def on_startup():
    init_db()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host=AppConfig.HOST, port=AppConfig.PORT, log_level=AppConfig.LOG_LEVEL)
