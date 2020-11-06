# Import all the models, so that Base has them before being
# imported by Alembic
from app.models.item import Item  # noqa
from app.models.user import User  # noqa
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id = Column(Integer, primary_key=True)
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
