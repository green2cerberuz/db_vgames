import functools
import os
from typing import Generator

import graphene
import pytest
from databases import Database, DatabaseURL
from fastapi.testclient import TestClient
from graphene.test import Client

from app.core.client import client_schema
from app.core.main import app
from app.db.session import SessionLocal
from app.db.utils import create_test_database, drop_database, run_test_migrations

TEST_DATABASE_URI = os.getenv("TEST_DATABASE_URI", False)


@pytest.fixture(scope="session")
def db() -> Generator:
    """Create a sqlalchemy local session for db."""
    yield SessionLocal()


@pytest.fixture(scope="session")
def async_db():
    """Create a databases instance for async support."""
    TEST_DATABASE_URI = os.getenv("TEST_DATABASE_URI")
    return Database(TEST_DATABASE_URI)


@pytest.fixture(scope="module")
def fast_api_client() -> Generator:
    """Instantiate a fast api client used for testing."""
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def graphene_client():
    client = Client(schema=client_schema)
    return client


# Taken from https://github.com/encode/databases/blob/master/tests/test_databases.py
# To create a new database for testing
@pytest.fixture(autouse=True, scope="module")
def setup_test_database():

    create_test_database()
    run_test_migrations()
    # Later see if could make a session with test database instead of main database.
    # session = SessionLocal()
    yield
    drop_database()
