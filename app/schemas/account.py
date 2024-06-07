from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict


class AccountBase(BaseModel):
    name: str
    description: str


class AccountCreate(AccountBase):
    balance: Decimal
    currency_id: int


class AccountUpdate(AccountBase):
    deleted: bool = False
    timestamp: Optional[datetime] = datetime.now()


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


class AccountData(BaseModel):
    id: int
    name: Optional[str]
    description: Optional[str]
    balance: Optional[Decimal] = None
    currency: Optional[str] = None

    @staticmethod
    def get_examples():
        examples = {
            200: {
                "description": "Successful Response",
                "content": {
                    "application/json": {
                        "examples": {
                            "with_balance": {
                                "summary": 'Сведения с балансом',
                                "value":  {
                                    "id": 1,
                                    "name": "Test account",
                                    "description": "Test account description",
                                    "balance": 100.98,
                                    "currency": "EUR"
                                }
                            },
                            "without_balance": {
                                "summary": 'Сведения без баланса',
                                "value": {
                                    "id": 2,
                                    "name": "Test account",
                                    "description": "Test account description"
                                }
                            },
                        }
                    }
                }
            },
        }
        return examples
