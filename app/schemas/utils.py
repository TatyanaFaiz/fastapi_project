from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict


class StatusTypes(str, Enum):
    success = "success"
    error = "error"


class BaseError(BaseModel):
    code: str
    description: Optional[str]


class BaseResult(BaseModel):
    status: StatusTypes
    error: Optional[BaseError]


class ValidationError(BaseResult):
    status: StatusTypes = StatusTypes.error
    error: BaseError

    model_config = ConfigDict(json_schema_extra={
            "example": {
                "status": "error",
                "error": {
                    "code": "validation_error",
                    "description": "Error description",
                }
            }
        })
