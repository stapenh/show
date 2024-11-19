from sqlmodel import Session, select
from app.models.messages import Message

# Функция для добавления сообщения
def create_message(session: Session, sender: str, receiver: str, content: str) -> Message:
    message = Message(sender=sender, receiver=receiver, content=content)
    session.add(message)
    session.commit()
    session.refresh(message)
    return message

# Функция для получения сообщений для определенного получателя
def get_messages_for_receiver(session: Session, receiver: str):
    query = select(Message).where(Message.receiver == receiver)
    return session.exec(query).all()
