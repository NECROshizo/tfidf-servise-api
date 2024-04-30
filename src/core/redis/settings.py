from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class RedisSettings(BaseSettings):
	"""Конфигурация Redis."""

	model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

	REDIS_DB: int = 1
	REDIS_HOST: str = "localhost"
	REDIS_PORT: int = 6379
	REDIS_USER: str = ""
	REDIS_PASSWORD: SecretStr


redis_settings = RedisSettings()
