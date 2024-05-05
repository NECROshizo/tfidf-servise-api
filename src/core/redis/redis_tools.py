from functools import wraps
import logging

from redis.asyncio import Redis, RedisError

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
	def __handle_redis_errors(method):
		@wraps(method)
		async def wrapper(*args, **kwargs):
			try:
				return await method(*args, **kwargs)
			except RedisError as e:
				logging.error(f"Ошибка выполнения запроса({method.__name__}) redis: {e}")
				raise

		return wrapper

	@__handle_redis_errors
	async def increment_or_create(self, key: str):
		return await self.__redis_client.hincrby("count", key)

	@__handle_redis_errors
	async def increment_docs(self):
		return await self.__redis_client.hincrby("docs", "docs_count")

	async def __aenter__(self) -> Redis:
		return self

	async def __aexit__(self, exc_type, exc_value, traceback):
		await self.__redis_client.aclose()


redis_tools = RedisTools(redis_settings)
