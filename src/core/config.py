
# Pydantic base settings read automatically from env variables
from pydantic import (
    BaseSettings,
    EmailStr,
    HttpUrl,
)

class Settings(BaseSettings):
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: str


settings = Settings()
