from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.graphene_pydantic import PydanticInputObjectType, PydanticObjectType


class ConsoleBase(BaseModel):
    """Console base class with basic fields  to get in fast api endpoints."""

    name: Optional[str] = None
    release_year: Optional[str] = None
    description: Optional[str] = None
    cover: Optional[str] = None
    description: Optional[str] = None
    motto: Optional[str] = None
    company_id: Optional[str] = None


class Console(ConsoleBase):
    """Properties to receive inside endpoint."""

    name: str
    company_id: str
    release_year: datetime


class ConsoleUpdate(ConsoleBase):
    """Properties to receive in update."""

    pass


class ConsoleDB(ConsoleBase):
    """Properties to return to client."""

    id: int

    class Config:
        orm_mode = True


class ConsoleInput(PydanticInputObjectType):
    """Pydantic validator class."""

    class Meta:
        model = ConsoleDB
        exclude_fields = (
            "id",
            "company_id",
        )


class ConsoleOutput(PydanticObjectType):
    """Pydantic validator class."""

    class Meta:
        model = ConsoleDB
