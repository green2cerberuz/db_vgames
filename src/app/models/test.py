from sqlalchemy import Column, String

from app.db.base_class import Base


class Test(Base):
    """Test class for project boilerplate."""

    name = Column(String(250), nullable=False)
