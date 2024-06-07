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


class BaseApiError(BaseResult):
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


class APIValidationError(Exception):
    def __init__(self, description: str):
        self.description = description
        self.content = {
            "status": "error",
            "error": {
                "code": "validation_error",
                "description": self.description,
            }
        }

    def __str__(self):
        if self.description:
            return f"{self.description}"
        else:
            return "Api Validation Error"
