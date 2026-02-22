from fastapi import FastAPI

app = FastAPI()

@app.get("/messages")
async def get_message():
    return {"message": ["message from message server"], "topic": "some"}

@app.get("/api/messages")
async def get_message():
    return {"message": ["message from message server"], "topic": "some"}

