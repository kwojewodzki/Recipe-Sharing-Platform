from typing import Union
from fastapi import FastAPI
from database import engine
import models

from database import get_session, init_db


app = FastAPI()


@app.get("/ping")
def read_root():
    return {"Ping": "Pong!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
