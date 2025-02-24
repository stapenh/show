# Используем базовый образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей
COPY services/requirements.txt .


# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt


# Копируем весь проект в контейнер
COPY . .


# Экспортируем переменные окружения
ENV PYTHONUNBUFFERED=1

# Запускаем приложение
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
