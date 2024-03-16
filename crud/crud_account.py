from typing import Optional

from sqlalchemy.orm import Session

from .base import CRUDBase
from models import LocalAccount, LocalCurrency
from schemas import AccountCreate, AccountUpdate


class CRUDAccount(CRUDBase[LocalAccount, AccountCreate, AccountUpdate]):
    def get_accounts_by_currency_code(self, db: Session,
                                      currency_code: str,
                                      skip: int = 0,
                                      limit: int = 1000
                                      ) -> Optional[list[LocalAccount]]:
        return (
            db.query(LocalAccount)
            .select_from(self.model)
            .join(LocalCurrency, LocalAccount.currency_id == LocalCurrency.id)
            .filter(LocalCurrency.code == currency_code)
            .filter(self.model.deleted.is_(False))
            .offset(skip)
            .limit(limit)
            .all()
        )


account = CRUDAccount(LocalAccount)
