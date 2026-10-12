from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()

class UserPayload(BaseModel):
    username: str
    age: int  # Automatically validated at ASGI request boundary

def get_db():
    # Dependency injected into request lifecycle
    db = {"status": "connected"}
    try:
        yield db
    finally:
        pass  # Auto cleanup post-response

@app.post("/users/")
async def create_user(payload: UserPayload, db=Depends(get_db)):
    return {"user": payload.username, "db_status": db["status"]}