from decimal import Decimal
from pydantic import BaseModel


class AccountBase(BaseModel):
    name: str
    description: str
    balance: Decimal
    currency_id: int


class AccountCreate(AccountBase):
    pass


class AccountUpdate(AccountBase):
    pass


# Properties shared by models stored in DB
class AccountInDBBase(AccountBase):
    id: int

    class Config:
        from_attributes = True


# Additional properties to return via API
class Account(AccountInDBBase):
    pass


# Additional properties stored in DB
class AccountInDB(AccountInDBBase):
    pass
