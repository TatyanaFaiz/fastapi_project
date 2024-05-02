from fastapi import FastAPI
import uvicorn

from app.core.config import settings
from app.core.openapi_tags import tags_metadata
from app.api.api_v1.api import api_router

app = FastAPI(title=settings.PROJECT_NAME,
              description=settings.PROJECT_DESCRIPTION,
              openapi_url=f"/{settings.API_URL}/v{settings.API_VERSION}/openapi.json",
              version=settings.API_VERSION,
              openapi_tags=tags_metadata)


app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
