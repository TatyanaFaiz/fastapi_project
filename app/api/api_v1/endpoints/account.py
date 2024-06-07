from fastapi import APIRouter, Depends, HTTPException
from pydantic import Field
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from app import crud
from app.api import deps
from app.schemas.account import AccountData
from app.schemas.utils import APIValidationError

router = APIRouter()


@router.get("/accounts/{account_id}", response_model=AccountData, responses=AccountData.get_examples(),
            response_model_exclude_unset=True)
async def get_account(
        *,
        db: Session = Depends(deps.get_db),
        account_id: int,
        with_balance: bool = False
):
    """
    Получение сведений лицевого счета
    """

    # if type(with_balance) is bool:
    #    return JSONResponse(status_code=422, content=APIValidationError("Parameter with_balance must be bool").content)

    account = crud.account.get(db=db, id=account_id)

    if not account:
        raise HTTPException(status_code=404, detail=f"Account with {account_id=} not found")

    response = AccountData(id=account_id,
                           name=account.name,
                           description=account.description)

    if not with_balance:
        return response

    currency = crud.currency.get(db=db, id=account.currency_id)
    if currency:
        response.currency = currency.name
        response.balance = account.balance

    return response
