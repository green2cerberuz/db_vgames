from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    """Declarative base class to use with SQLAlchemy."""

    id = Column(Integer, primary_key=True)

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        """Conver tables name to lowercase."""
        return cls.__name__.lower()
