import functools
import os

import pytest
from databases import Database
from sqlalchemy.orm import Session

TEST_DATABASE_URI = os.getenv("TEST_DATABASE_URI", False)


def async_adapter(wrapped_func):
    """
    Decorator used to run async test cases.
    """

    @functools.wraps(wrapped_func)
    def run_sync(*args, **kwargs):
        loop = asyncio.new_event_loop()
        task = wrapped_func(*args, **kwargs)
        return loop.run_until_complete(task)


def test_env_variables() -> None:
    assert os.getenv("POSTGRES_USER", False) is not False
    assert os.getenv("POSTGRES_PASSWORD", False) is not False
    assert os.getenv("POSTGRES_DB", False) is not False
    assert os.getenv("DATABASE_URI", False) is not False
    assert os.getenv("TEST_DATABASE_URI", False) is not False
    assert os.getenv("TEST_DB_NAME", False) is not False


def test_db_connection(db: Session) -> None:
    proxy_result = db.execute("SELECT 1")
    result = proxy_result.fetchall()
    assert result == [(1,)]


@pytest.mark.asyncio
async def test_async_db_connection():
    """
    Test simple asyncronous connection to database
    """
    TEST_DATABASE_URI = os.getenv("TEST_DATABASE_URI")
    async with Database(TEST_DATABASE_URI) as database:
        result = await database.execute("SELECT 1")
        assert result == 1
