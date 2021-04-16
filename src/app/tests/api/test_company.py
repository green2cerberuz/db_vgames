import asyncio

import pytest
from graphql.execution.executors.asyncio import AsyncioExecutor


def test_create_company(fast_api_client, graphene_client):
    query = """
    mutation {
        createCompany(companyDetails: {
            name:"nintendo",
            description:"awesome company",
            logo: "siempre olvidada",
            creationYear: "2020-12-04 12:23:44",
            isPublisher: true,
        })
        {
            id
            name
            description
            isPublisher
        }
    }
    """
    result = graphene_client.execute(
        query,
        executor=AsyncioExecutor(),
    )
    assert result["data"]["createCompany"]["id"] == 1


def test_query_companies(fast_api_client, graphene_client):
    query = """
    query {
        companies
        {
            id
            name
            description
            isPublisher
        }
    }
    """
    result = graphene_client.execute(
        query,
        executor=AsyncioExecutor(),
    )
    assert len(result["data"]["companies"]) == 1
