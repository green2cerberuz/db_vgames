from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

from .association import game_console_table


class Game(Base):
    """Game model: Show basic info of games stored in database."""

    name = Column(String(250), nullable=False)
    publication_year = Column(DateTime)
    score = Column(Integer)
    description = Column(String(500))
    cover = Column(String(500))

    # Many2Many console relationship.
    consoles = relationship("Console", secondary=game_console_table, backref="games")

    # One 2 many saga relationship.
    franchise_id = Column(Integer, ForeignKey("franchise.id", ondelete="CASCADE"))
    franchise = relationship("Franchise", backref="games")

    def __repr__(self):
        """Return human readeable object representation."""
        return f"Game({self.name})"
