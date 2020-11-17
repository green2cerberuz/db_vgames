from fastapi import FastAPI
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp

from app.db.async_db import database
from app.models.game import Game

from .api.client import client_schema

app = FastAPI()
app.add_route(
    "/graphql/client", GraphQLApp(schema=client_schema, executor_class=AsyncioExecutor)
)


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


@app.post("/games/")
async def create_game():
    """Create a games object in database asyncronously."""
    games = Game.__table__
    query = games.insert().values(name="Final fantasy 7")
    last_record_id = await database.execute(query)
    return {"id": last_record_id}
