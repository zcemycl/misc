from pydantic import BaseSettings, Field


class DbConfig(BaseSettings):
    db_async_connection_str: str


class Settings(BaseSettings):
    api_v1_prefix: str
    debug: bool
    project_name: str
    version: str
    description: str
    # base: BaseConfig = Field(default_factory = BaseConfig)
    db: DbConfig = Field(default_factory = DbConfig)