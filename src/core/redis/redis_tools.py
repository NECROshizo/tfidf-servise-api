# from redis.asyncio import Redis # TODO: asyn? async witch
from functools import wraps
import logging
from redis import Redis, RedisError

from src.core.redis import RedisSettings, redis_settings


class RedisTools:
	def __init__(self, settings: RedisSettings):
		self.setting = settings
		self.__redis_client = Redis(
			host=settings.REDIS_HOST,
			port=settings.REDIS_PORT,
			password=settings.REDIS_PASSWORD.get_secret_value(),
			db=settings.REDIS_DB,
			decode_responses=True,
		)

	@staticmethod
	def __check_error(method):
		@wraps(method)
		def wrapper(*args, **kwargs):
			try:
				return method(*args, **kwargs)
			except RedisError as e:
				logging.error(f"Ошибка выполнения запроса redis: {e}")
				raise

		return wrapper

	@__check_error
	def increment_or_create(self, key: str):
		return self.__redis_client.hincrby("count", key)

	@__check_error
	def increment_docs(self):
		return self.__redis_client.hincrby("docs", "docs_count")


redis_tools = RedisTools(redis_settings)
