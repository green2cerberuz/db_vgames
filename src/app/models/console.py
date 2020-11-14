from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Console(Base):
    """Console model: Show basic info of games stored in database."""

    name = Column(String(250), nullable=False)
    release_year = Column(DateTime, nullable=False)
    description = Column(String(500))
    cover = Column(String(500))
    motto = Column(String(100), nullable=False)
    company_id = Column(Integer, ForeignKey("company.id", ondelete="CASCADE"))
    company = relationship("Company", backref="consoles")

    def __repr__(self):
        """Return human readeable object representation."""
        return f"Console({self.name},{self.motto},{self.release_year})"
