import asyncio

import pytest
from graphql.execution.executors.asyncio import AsyncioExecutor

from app.core.main import startup


def test_create_console(fast_api_client, graphene_client):
    query = """
    mutation {
        createConsole(consoleDetails: {
            name: "GameCube",
            releaseYear: "2020-01-18 13:55:44",
            description: "A Family console",
            cover: "http:localhost:8000/blacksheepwall",
            motto: "life is hard, make it simple",
        })
        {
            id
            name
            description
        }
    }
    """
    result = graphene_client.execute(
        query,
        executor=AsyncioExecutor(),
    )
    assert result["data"]["createConsole"]["id"] == 1


# @pytest.mark.asyncio
# async def test_async_db_connection():
#     """
#     Test simple asyncronous connection to database
#     """
#     TEST_DATABASE_URI = os.getenv("TEST_DATABASE_URI")
#     async with Database(TEST_DATABASE_URI) as database:
#         result = await database.execute("SELECT 1")
#         assert result == 1
