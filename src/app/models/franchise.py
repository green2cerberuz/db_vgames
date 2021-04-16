from sqlalchemy import Column, DateTime, String

from app.db.base_class import Base


class Franchise(Base):
    """Game model: Show basic info of games stored in database."""

    title = Column(String(250), nullable=False)
    first_release = Column(DateTime)
    description = Column(String(250))

    def __repr__(self):
        """Return human readeable object representation."""
        return f"Franchise({self.title})"
