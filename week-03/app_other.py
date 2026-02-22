from fastapi import FastAPI

app = FastAPI()

@app.get("/api/other")
async def get_other():
    return {"other": "message from other server"}
