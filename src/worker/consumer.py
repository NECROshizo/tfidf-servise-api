from abc import ABC, abstractmethod
import asyncio
import logging
from typing import Any, Coroutine, TypeVar

from aio_pika import connect_robust
from aio_pika.abc import AbstractChannel, AbstractRobustConnection, AbstractIncomingMessage

from src.core.rabbit.settings import RabbitSettings, rabbit_settings
from src.core.services import get_tf_idf

T = TypeVar("T")


class AbstractRabbitConsumer(ABC):
	"""Abstract publisher."""

	settings: RabbitSettings = rabbit_settings

	def __init__(self, routing_key: str) -> None:
		self.routing_key = routing_key

	def _get_connection(self) -> Coroutine[Any, Any, AbstractRobustConnection]:
		return connect_robust(self.settings.rabbitmq_url)

	@abstractmethod
	async def consume(self, message: T) -> None:
		"""Publish message."""
		...


class WorkerRabbitConsumer(AbstractRabbitConsumer):
	async def close(self) -> None:
		await self.channel.close()
		self.connection = None

	async def consume(self) -> None:
		try:
			async with await self._get_connection() as connection:
				channel: AbstractChannel = await connection.channel()
				queue = await channel.declare_queue(self.routing_key)
				await queue.consume(self._message_callback)
				await asyncio.Future()
		except Exception as e:
			logging.error(f"Ошибка подключения к брокеру сообщений: {e}")

	async def consume_one_message(self) -> None:
		try:
			async with await self._get_connection() as connection:
				channel: AbstractChannel = await connection.channel()

				queue = await channel.declare_queue(self.routing_key)
				message = await queue.get(fail=False)
				if message:
					return await self._message_callback(message)
					# return dict(**json.loads(message.body.decode()))
		except Exception as e:
			logging.error(f"Ошибка подключения к брокеру сообщений: {e}")

	async def _message_callback(self, message: AbstractIncomingMessage) -> None:
		try:
			# print(message.body.decode())
			result = await get_tf_idf(message.body)
			print(result, message.message_id)
			# await rollbac_result()
			# publisher = WorkerRabbitSubPublisher("revers_hell")
			# await publisher.publish(result, message.message_id)

		except Exception as e:
			logging.error(f"Ошибка при обработки сообщения: {e}")
			await message.nack()
			raise
		finally:
			await message.ack()
