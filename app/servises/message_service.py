messages_db = []

async def send_message(message):
    messages_db.append(message.dict())
    return {"status": "Message sent"}

async def receive_message(receiver):
    return [msg for msg in messages_db if msg["receiver"] == receiver]
