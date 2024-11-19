from sqlmodel import SQLModel, create_engine, Session


DATABASE_URL = "sqlite:///messages.db"  # Используем SQLite для простоты

engine = create_engine(DATABASE_URL, echo=True)  # echo=True для отладки SQL-запросов

# Функция для инициализации базы данных
def init_db():
    import app.models.messages  # Импортируем модели перед созданием таблиц
    SQLModel.metadata.create_all(engine)

# Функция для получения сессии
def get_session():
    with Session(engine) as session:
        yield session

