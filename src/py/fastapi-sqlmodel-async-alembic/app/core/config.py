from pydantic import BaseSettings, Field


class BaseConfig(BaseSettings):
    api_v1_prefix: str
    debug: bool
    project_name: str
    version: str
    description: str


class DbConfig(BaseSettings):
    db_async_connection_str: str


class Settings(BaseSettings):
    base: BaseConfig = Field(default_factory = BaseConfig)
    db: DbConfig = Field(default_factory = DbConfig)