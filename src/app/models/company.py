from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.ext.hybrid import hybrid_property

from app.db.base_class import Base


class Company(Base):
    """Company model: Show basic info of video game companies."""

    name = Column(String(250), nullable=False)
    creation_year = Column(DateTime)
    description = Column(String(500))
    logo = Column(String(500))
    is_publisher = Column(Boolean)

    @hybrid_property
    def total_consoles(self):
        """Return count of total games of a company that user have."""
        if hasattr(self, "consoles"):
            return self.consoles.count()
        return 0

    def __repr__(self):
        """Return human readeable object representation."""
        return f"Company({self.name}"
