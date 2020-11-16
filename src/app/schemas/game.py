from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class GameBase(BaseModel):
    """Game base class to show in ffast api endpoints."""

    name: str
    description: Optional[str] = None
    publication_year: Optional[datetime] = None
    score: Optional[int] = None
    cover: Optional[str] = None

    class Config:
        orm_mode = True
