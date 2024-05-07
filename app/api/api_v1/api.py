from fastapi import APIRouter

from app.api.api_v1.endpoints import account
from app.schemas.utils import ValidationError

responses = {
    422: {'model': ValidationError, 'description': 'Validation Error'}
}

api_router = APIRouter()
api_router.include_router(account.router, tags=["accounts"], responses=responses)
