from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    DATASET: str
    FILE: str
    DATABASE_URL: str
    SEED: int
    VALID_SIZE: float
