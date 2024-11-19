
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Message(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # Автоматический ID
    sender: str  # Имя отправителя
    receiver: str  # Имя получателя
    content: str  # Содержание сообщения
    timestamp: datetime = Field(default_factory=datetime.utcnow)  # Временная метка
