from fastapi import APIRouter

from app.api.api_v1.endpoints import account
from app.schemas.utils import BaseApiError, BaseResult

responses = {
    422: {'model': BaseApiError, 'description': 'Validation Error'},
    404: {
        'model': BaseResult,
        'description': 'Not Found Error',
        "content": {
            "application/json": {
                "example": {"detail": "Error description"}
            }
        }
    }
}

api_router = APIRouter()
api_router.include_router(account.router, tags=["accounts"], responses=responses)
