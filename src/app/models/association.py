from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship

from app.db.base_class import Base

game_console_table = Table(
    "game_console_table",
    Base.metadata,
    Column("game_id", Integer, ForeignKey("game.id")),
    Column("console_id", Integer, ForeignKey("console.id")),
)

game_tag_table = Table(
    "game_tag_table",
    Base.metadata,
    Column("game_id", Integer, ForeignKey("game.id")),
    Column("tag_id", Integer, ForeignKey("tag.id")),
)


class FranchiseAssociation(Base):
    """Association table to make queries faster between franchise, consoles and games."""

    franchise_id = Column(Integer, ForeignKey("franchise.id", ondelete="CASCADE"))
    franchise = relationship("Franchise", backref="related_franchise")

    game_id = Column(Integer, ForeignKey("game.id", ondelete="CASCADE"))
    game = relationship("Games", backref="related_franchise")

    console_id = Column(Integer, ForeignKey("console.id", ondelete="CASCADE"))
    console = relationship("Console", backref="related_franchise")

    def __repr__(self):
        """Return human readeable object representation."""
        return f"{self.franchise.title}-{self.game.name}"
