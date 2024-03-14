from pydantic import BaseModel


class CurrencyBase(BaseModel):
    pass


class CurrencyCreate(CurrencyBase):
    pass


class CurrencyUpdate(CurrencyBase):
    pass


# Properties shared by models stored in DB
class CurrencyInDBBase(CurrencyBase):
    pass

    class Config:
        from_attributes = True


# Additional properties to return via API
class Currency(CurrencyInDBBase):
    pass


# Additional properties stored in DB
class CurrencyInDB(CurrencyInDBBase):
    pass
