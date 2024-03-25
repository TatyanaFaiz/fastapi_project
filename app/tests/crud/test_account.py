from faker import Faker
from sqlalchemy.orm import Session

from app import crud
from app.schemas import CurrencyCreate


def test_get_accounts_by_currency_code(faker: Faker, db: Session) -> None:
    currency = crud.currency.create(db=db, obj_in=CurrencyCreate(name='test_currency', code='999'))
    assert currency is not None

    account_balance = faker.random_int(min=1, max=999999)
    data_obj = {
        'name': 'Test name',
        'description': 'Test description',
        'balance': account_balance,
        'currency_id': currency.id
    }
    first_account = crud.account.create(db=db, obj_in=data_obj)
    assert first_account is not None

    second_account = crud.account.create(db=db, obj_in=data_obj)
    assert second_account is not None

    accounts_by_code = crud.account.get_accounts_by_currency_code(db=db, currency_code='999')
    assert accounts_by_code is not None
    assert len(accounts_by_code) == 2

    deleted_first_account = crud.account.remove(db=db, id=first_account.id)
    assert deleted_first_account is not None

    deleted_second_account = crud.account.remove(db=db, id=second_account.id)
    assert deleted_second_account is not None

    deleted_currency = crud.currency.remove(db=db, id=currency.id)
    assert deleted_currency is not None


def test_not_found_accounts(db: Session) -> None:
    accounts_by_code = crud.account.get_accounts_by_currency_code(db=db, currency_code='111')
    assert accounts_by_code is not None
    assert len(accounts_by_code) == 0
