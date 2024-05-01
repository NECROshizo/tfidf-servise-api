from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class RabbitSettings(BaseSettings):
	"""Класс импорта переменных окружения."""

	model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

	RABBITMQ_HOST: str
	RABBITMQ_PORT: int
	RABBITMQ_USER: str
	RABBITMQ_PASSWORD: SecretStr

	@property
	def rabbitmq_url(self) -> str:
		return (
			f"amqp://{self.RABBITMQ_USER}:{self.RABBITMQ_PASSWORD.get_secret_value()}"
			f"@{self.RABBITMQ_HOST}:{self.RABBITMQ_PORT}//"
		)


rabbit_settings = RabbitSettings()
