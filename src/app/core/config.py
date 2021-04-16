"""Setup settings variables to all modules."""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Class to map directly all needed env variable."""

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_URI: str


settings = Settings()
