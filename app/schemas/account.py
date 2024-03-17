from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class AccountBase(BaseModel):
    name: str
    description: str


class AccountCreate(AccountBase):
    balance: Decimal
    currency_id: int


class AccountUpdate(AccountBase):
    deleted: bool
    timestamp: datetime


# Properties shared by models stored in DB
class AccountInDBBase(AccountBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


# Additional properties to return via API
class Account(AccountInDBBase):
    pass


# Additional properties stored in DB
class AccountInDB(AccountInDBBase):
    pass