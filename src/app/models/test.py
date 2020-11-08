from app.db.base_class import Base
from sqlalchemy import Column, String


class Test(Base):
    name = Column(String(250), nullable=False)
