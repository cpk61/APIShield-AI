from fastapi import FastAPI
from pydantic import BaseModel
from core import APIShield

app = FastAPI(title='APIShield AI')
shield = APIShield()

class Event(BaseModel):
    client_id: str
    status_code: int
    latency_ms: float
    path: str

@app.post('/inspect')
def inspect(e: Event):
    return shield.inspect(**e.model_dump())
