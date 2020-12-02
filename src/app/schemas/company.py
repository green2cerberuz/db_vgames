from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.graphene_pydantic import PydanticInputObjectType, PydanticObjectType


class CompanyBase(BaseModel):
    """Console base class with basic fields  to get in fast api endpoints."""

    name: Optional[str] = None
    creation_year: Optional[str] = None
    description: Optional[str] = None
    logo: Optional[str] = None
    is_publisher: Optional[bool] = None


class Company(CompanyBase):
    """Properties to receive inside endpoint."""

    name: str
    company_id: str
    release_year: datetime


class CompanyUpdate(CompanyBase):
    """Properties to receive in update."""

    pass


class CompanyDB(CompanyBase):
    """Properties to return to client."""

    id: int

    class Config:
        orm_mode = True


class CompanyInput(PydanticInputObjectType):
    """Pydantic validator class."""

    class Meta:
        model = CompanyDB
        exclude_fields = ("id",)


class CompanyUpdateInput(PydanticInputObjectType):
    """Pydantic validator class."""

    class Meta:
        model = CompanyDB


class CompanyOutput(PydanticObjectType):
    """Pydantic validator class."""

    class Meta:
        model = CompanyDB
