from typing import Optional, Union

from pydantic import PostgresDsn, field_validator, AnyHttpUrl
from pydantic_core.core_schema import ValidationInfo
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str

    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @classmethod
    @field_validator('SQLALCHEMY_DATABASE_URI', mode='after')
    def assemble_db_connection(cls, v: PostgresDsn, values: ValidationInfo) -> PostgresDsn:
        if v is not None:
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            username=values.data.get("POSTGRES_USER"),
            password=values.data.get("POSTGRES_PASSWORD"),
            host=values.data.get("POSTGRES_SERVER"),
            port=values.data.get("POSTGRES_PORT"),
            path=values.data.get("POSTGRES_DB"),
        )

    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []

    @classmethod
    @field_validator('BACKEND_CORS_ORIGINS')
    def assemble_cors_origins(cls, v: Union[str, list[str]]) -> Union[list[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', case_sensitive=True)


settings = Settings()
