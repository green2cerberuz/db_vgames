import os

from sqlalchemy.orm import Session


def test_env_variables(db: Session) -> None:
    assert os.getenv("POSTGRES_USER", False) is not False
    assert os.getenv("POSTGRES_PASSWORD", False) is not False
    assert os.getenv("POSTGRES_DB", False) is not False
    assert os.getenv("DATABASE_URI", False) is not False


def test_db_connection(db: Session) -> None:
    proxy_result = db.execute("SELECT 1")
    result = proxy_result.fetchall()
    assert result == [(1,)]
