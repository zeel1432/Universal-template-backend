from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str = "CHANGE_ME"

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
