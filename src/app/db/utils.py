import logging
import os

import psycopg2
import sqlalchemy
from sqlalchemy import create_engine

from alembic import command
from alembic.config import Config


def run_test_migrations():
    """Run alembic migrations inside test database."""
    # Check docs to see alembic commands api:
    # https://alembic.sqlalchemy.org/en/latest/api/commands.html
    # https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config
    script_location = os.getenv("SCRIPT_LOCATION")
    database_uri = os.getenv("TEST_DATABASE_URI")
    logging.info("Running DB migrations in %r on %r", script_location, database_uri)
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("script_location", script_location)
    alembic_cfg.set_main_option("sqlalchemy.url", database_uri)
    command.upgrade(alembic_cfg, "head")


def create_test_database():
    """Create a test database everytime a new test module is being run by pytest."""
    TEST_DB_NAME = os.getenv("TEST_DB_NAME")

    test_engine = create_engine(
        "postgresql://postgres:postgres@db:5432/postgres", echo=False
    )
    create_db = True
    conn = test_engine.connect()
    conn = conn.execution_options(autocommit=False)
    conn.execute("ROLLBACK")
    try:
        conn.execute("DROP DATABASE %s" % TEST_DB_NAME)
    except (sqlalchemy.exc.ProgrammingError, psycopg2.errors.InvalidCatalogName) as e:
        # Could not drop the database, probably does not exist
        print(e)
        conn.execute("ROLLBACK")
    except (sqlalchemy.exc.OperationalError) as e:
        # Could not drop database because it's being accessed by other users (psql prompt open?)
        print(e)
        conn.execute("ROLLBACK")
        create_db = False
        print("Something happened when deleting test database.")
    if create_db:
        try:
            conn.execute("CREATE DATABASE %s" % TEST_DB_NAME)
        except Exception as e:
            print(e)
            conn.execute("ROLLBACK")
    conn.close()
    test_engine.dispose()


def drop_database():
    """Drop especified database."""
    TEST_DB_NAME = os.getenv("TEST_DB_NAME")

    test_engine = create_engine(
        "postgresql://postgres:postgres@db:5432/postgres", echo=False
    )
    conn = test_engine.connect()
    conn = conn.execution_options(autocommit=False)
    conn.execute("ROLLBACK")
    try:
        conn.execute("DROP DATABASE %s" % TEST_DB_NAME)
    except (sqlalchemy.exc.ProgrammingError, psycopg2.errors.InvalidCatalogName) as e:
        # Could not drop the database, probably does not exist
        print(e)
        conn.execute("ROLLBACK")
    except (sqlalchemy.exc.OperationalError) as e:
        # Could not drop database because it's being accessed by other users (psql prompt open?)
        print(e)
        conn.execute("ROLLBACK")
