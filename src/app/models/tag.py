from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

from .association import game_tag_table


class Tag(Base):
    """Tag model: To show game genere."""

    name = Column(String(250), nullable=False)

    # Many2Many console relationship.
    games = relationship("Game", secondary=game_tag_table, backref="tags")

    def __repr__(self):
        """Return human readeable object representation."""
        return f"Tag({self.name})"
