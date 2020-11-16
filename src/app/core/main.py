from typing import Optional

from fastapi import FastAPI

from app.db.async_db import database
from app.models.game import Game

app = FastAPI()


@app.on_event("startup")
async def startup():
    """Connect to database at fast api start."""
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    """When fast api stops disconnect from database."""
    await database.disconnect()


@app.get("/")
def read_root():
    """Home route for testing."""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    """Return url parameters for testing."""
    return {"item_id": item_id, "q": q}


@app.post("/games/")
async def create_game():
    """Create a games object in database asyncronously."""
    games = Game.__table__
    query = games.insert().values(name="Final fantasy 7")
    last_record_id = await database.execute(query)
    return {"id": last_record_id}
