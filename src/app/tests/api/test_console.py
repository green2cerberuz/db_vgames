import asyncio

import pytest
from graphql.execution.executors.asyncio import AsyncioExecutor


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


def test_update_console(fast_api_client, graphene_client):
    query = """
    mutation {
        updateConsole(consoleDetails: {
            id: 1,
            name: "GameCube Updated",
            description: "A Family console with a nice touch",
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
    assert result["data"]["updateConsole"]["name"] != "GameCube"
    assert result["data"]["updateConsole"]["name"] == "GameCube Updated"


def test_delete_console(fast_api_client, graphene_client):
    query = """
    mutation {
        deleteConsole(consoleId: 1) {
            response
        }
    }
    """
    result = graphene_client.execute(
        query,
        executor=AsyncioExecutor(),
    )
    assert result["data"]["deleteConsole"]["response"]["ok"] == True


def test_fail_delete_console(fast_api_client, graphene_client):
    query = """
    mutation {
        deleteConsole(consoleId: 2) {
            response
        }
    }
    """
    result = graphene_client.execute(
        query,
        executor=AsyncioExecutor(),
    )
    assert result["data"]["deleteConsole"]["response"]["ok"] == False
