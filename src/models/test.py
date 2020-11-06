from db.base import Base
from sqlalchemy import Column, String


class Test(Base):
    name = Column(String(250), nullable=False)
