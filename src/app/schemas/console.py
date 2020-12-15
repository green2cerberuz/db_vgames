from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from app.graphene_pydantic import PydanticInputObjectType, PydanticObjectType
from app.schemas.company import CompanyDB


class ConsoleBase(BaseModel):
    """Console base class with basic fields  to get in fast api endpoints."""

    name: Optional[str] = None
    release_year: Optional[str] = None
    description: Optional[str] = None
    cover: Optional[str] = None
    description: Optional[str] = None
    motto: Optional[str] = None
    company_id: Optional[int] = None
    # FIXME: this should work but it does not, need to check it for references
    # company: Optional[List[Company]] = None


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
    company: Optional[List[CompanyDB]]

    class Config:
        orm_mode = True


class ConsoleInput(PydanticInputObjectType):
    """Pydantic validator class."""

    class Meta:
        model = ConsoleDB
        exclude_fields = ("id",)


class ConsoleUpdateInput(PydanticInputObjectType):
    """Pydantic validator class."""

    class Meta:
        model = ConsoleDB
        # exclude_fields = ("company_id",)


class ConsoleOutput(PydanticObjectType):
    """Pydantic validator class."""

    class Meta:
        model = ConsoleDB
