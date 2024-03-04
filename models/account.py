from sqlalchemy import Column, Integer, String
from database.base import Base


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

