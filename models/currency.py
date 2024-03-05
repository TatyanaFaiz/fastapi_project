from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, func
from database.base import Base


class Currency(Base):
    __tablename__ = "currency"

    id = Column(Integer, primary_key=True)
    timestamp = Column(TIMESTAMP(True), server_default=func.now())
    deleted = Column(Boolean, server_default='f')
    name = Column(String)
    code = Column(String(3), default=None, nullable=True)
