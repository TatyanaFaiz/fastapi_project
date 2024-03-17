from .base import CRUDBase
from app.models import LocalCurrency
from app.schemas import CurrencyCreate, CurrencyUpdate


class CRUDCurrency(CRUDBase[LocalCurrency, CurrencyCreate, CurrencyUpdate]):
    pass


currency = CRUDCurrency(LocalCurrency)
