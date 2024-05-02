from fastapi import APIRouter

router = APIRouter()


@router.get("/accounts/{account_id}")
async def read_item(account_id: int):
    """
    Получение сведений лицевого счета
    """
    return {"account_id": account_id}
