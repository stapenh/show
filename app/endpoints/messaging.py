from fastapi import APIRouter, Depends
from database.database import get_session
from database.massage_crud import create_message, get_messages_for_receiver
from app.models.messages import Message
from sqlmodel import Session

router = APIRouter(prefix="/messages", tags=["Messages"])

@router.post("/")
async def create_message_endpoint(
    message: Message, session: Session = Depends(get_session)
):
    return create_message(session, message.sender, message.receiver, message.content)

@router.get("/{receiver}")
async def get_messages_endpoint(receiver: str, session: Session = Depends(get_session)):
    return get_messages_for_receiver(session, receiver)
