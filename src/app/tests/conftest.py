from typing import Generator

import pytest

from app.core.main import app
from app.db.session import SessionLocal
from fastapi.testclient import TestClient


@pytest.fixture(scope="session")
def db() -> Generator:
    """Create a sqlalchemy local session for db."""
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    """Instantiate a fast api client used for testing."""
    with TestClient(app) as c:
        yield c
