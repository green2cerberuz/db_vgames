"""Setup settings variables to all modules."""
import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Class to map directly all needed env variable."""

    print(os.environ)
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_URI: str


settings = Settings()
