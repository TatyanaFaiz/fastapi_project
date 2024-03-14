from .base import CRUDBase
from models import LocalCurrency
from schemas import CurrencyCreate, CurrencyUpdate


class CRUDCurrency(CRUDBase[LocalCurrency, CurrencyCreate, CurrencyUpdate]):
    pass


currency = CRUDCurrency(LocalCurrency)
