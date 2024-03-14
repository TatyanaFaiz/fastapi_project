from .base import CRUDBase
from models import LocalAccount
from schemas import AccountCreate, AccountUpdate


class CRUDAccount(CRUDBase[LocalAccount, AccountCreate, AccountUpdate]):
    pass


account = CRUDAccount(LocalAccount)
