from sqlalchemy import Column, Integer, String, TIMESTAMP, func, Boolean, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship

from database.base import Base


class LocalAccount(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True)
    timestamp = Column(TIMESTAMP(True), server_default=func.now())
    deleted = Column(Boolean, server_default='f')
    name = Column(String)
    description = Column(String)
    balance = Column(DECIMAL)
    currency_id = Column(Integer, ForeignKey("currency.id"))
    currency = relationship("LocalCurrency", back_populates="account")
