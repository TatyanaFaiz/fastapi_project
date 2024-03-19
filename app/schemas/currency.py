from typing import Annotated

from pydantic import BaseModel, ConfigDict, StringConstraints


class CurrencyBase(BaseModel):
    name: str
    code: Annotated[str, StringConstraints(max_length=3)]


class CurrencyCreate(CurrencyBase):
    pass


class CurrencyUpdate(CurrencyBase):
    pass


# Properties shared by models stored in DB
class CurrencyInDBBase(CurrencyBase):
    model_config = ConfigDict(from_attributes=True)


# Additional properties to return via API
class Currency(CurrencyInDBBase):
    pass


# Additional properties stored in DB
class CurrencyInDB(CurrencyInDBBase):
    pass
