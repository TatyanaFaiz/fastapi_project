from faker import Faker
from sqlalchemy.orm import Session

from app import crud
from app.schemas import CurrencyCreate, AccountUpdate


def test_create(db: Session) -> None:
    currency = crud.currency.create(db=db, obj_in=CurrencyCreate(name='test_currency', code='999'))
    assert currency is not None
    assert currency.name == 'test_currency'
    assert currency.code == '999'

    deleted_currency = crud.currency.remove(db=db, id=currency.id)
    assert deleted_currency is not None
    assert deleted_currency.id == currency.id


def test_get(faker: Faker, db: Session) -> None:
    currency = crud.currency.create(db=db, obj_in=CurrencyCreate(name='test_currency', code='999'))
    assert currency is not None

    test_currency = crud.currency.get(db=db, id=currency.id)
    assert test_currency is not None
    assert test_currency.id == currency.id
    assert test_currency.name == 'test_currency'
    assert test_currency.code == '999'

    account_balance = faker.random_int(min=1, max=999999)
    data_obj = {
        'name': 'Test name',
        'description': 'Test description',
        'balance': account_balance,
        'currency_id': test_currency.id
    }
    account = crud.account.create(db=db, obj_in=data_obj)
    assert account is not None

    test_account = crud.account.get(db=db, id=account.id)
    assert test_account.id is not None
    assert test_account.id == account.id
    assert test_account.name == 'Test name'
    assert test_account.description == 'Test description'
    assert test_account.balance == account_balance
    assert test_account.currency_id == account.currency_id

    deleted_account = crud.account.remove(db=db, id=account.id)
    assert deleted_account is not None

    deleted_currency = crud.currency.remove(db=db, id=currency.id)
    assert deleted_currency is not None


def test_get_by(faker: Faker, db: Session) -> None:
    currency = crud.currency.create(db=db, obj_in=CurrencyCreate(name='test_currency', code='999'))
    assert currency is not None

    account_balance = faker.random_int(min=1, max=999999)
    data_obj = {
        'name': 'Test name',
        'description': 'Test description',
        'balance': account_balance,
        'currency_id': currency.id
    }
    account = crud.account.create(db=db, obj_in=data_obj)
    assert account is not None

    test_account = crud.account.get_by(db=db, id=account.id, name='Test name')
    assert test_account.id is not None
    assert test_account.id == account.id
    assert test_account.name == 'Test name'
    assert test_account.description == 'Test description'
    assert test_account.balance == account_balance
    assert test_account.currency_id == account.currency_id

    deleted_account = crud.account.remove(db=db, id=account.id)
    assert deleted_account is not None

    deleted_currency = crud.currency.remove(db=db, id=currency.id)
    assert deleted_currency is not None


def test_update(faker: Faker, db: Session) -> None:
    currency = crud.currency.create(db=db, obj_in=CurrencyCreate(name='test_currency', code='999'))
    assert currency is not None

    account_balance = faker.random_int(min=1, max=999999)
    data_obj = {
        'name': 'Test name',
        'description': 'Test description',
        'balance': account_balance,
        'currency_id': currency.id
    }
    account = crud.account.create(db=db, obj_in=data_obj)
    assert account is not None

    obj_in = AccountUpdate(name='New test name', description='New test description')
    update_account = crud.account.update(db=db, db_obj=account, obj_in=obj_in)

    assert update_account is not None
    assert update_account.id == account.id
    assert update_account.name == obj_in.name
    assert update_account.description == obj_in.description
    assert update_account.balance == account.balance

    deleted_account = crud.account.remove(db=db, id=account.id)
    assert deleted_account is not None

    deleted_currency = crud.currency.remove(db=db, id=currency.id)
    assert deleted_currency is not None


