import functools
import os
from typing import Generator

import pytest
from databases import Database, DatabaseURL
from fastapi.testclient import TestClient

from app.core.main import app
from app.db.session import SessionLocal

TEST_DATABASE_URI = os.getenv("TEST_DATABASE_URI", False)


@pytest.fixture(scope="session")
def db() -> Generator:
    """Create a sqlalchemy local session for db."""
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    """Instantiate a fast api client used for testing."""
    with TestClient(app) as c:
        yield c


# Taken from https://github.com/encode/databases/blob/master/tests/test_databases.py
# To create a new database for testing
@pytest.fixture(autouse=True, scope="module")
def create_test_database():
    # Create test databases with tables creation
    database_url = DatabaseURL(TEST_DATABASE_URI)
    session = SessionLocal()
    # Run the test suite
    yield

    # Drop test databases
    # maybe
    pass
