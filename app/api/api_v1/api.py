from fastapi import APIRouter

from app.api.api_v1.endpoints import account

api_router = APIRouter()
api_router.include_router(account.router, tags=["accounts"])
