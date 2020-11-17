from datetime import datetime
from typing import Optional

from graphene_pydantic import PydanticObjectType
from pydantic import BaseModel


class ConsoleBase(BaseModel):
    """Console base class with basic fields  to get in fast api endpoints."""

    name: Optional[str] = None
    release_year: Optional[datetime] = None
    description: Optional[str] = None
    cover: Optional[str] = None
    description: Optional[str] = None
    motto: Optional[int] = None
    company_id: Optional[str] = None


class Console(ConsoleBase):
    """Properties to receive inside endpoint."""

    name: str
    company_id: str
    release_year: datetime


class ConsoleUpdate(ConsoleBase):
    """Properties to receive in update."""

    pass


class ConsoleInDBBase(ConsoleBase):
    """Properties shared by models stored in DB."""

    id: int

    class Config:
        orm_mode = True


class ConsoleDB(ConsoleInDBBase):
    """Properties to return to client."""

    pass


class ConsoleGrapheneModel(PydanticObjectType):
    """Pydantic validator class."""

    class Meta:
        model = ConsoleDB
