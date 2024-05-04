from abc import ABC, abstractmethod
import json
import logging
from typing import Any, Coroutine, TypeVar

from aio_pika import Message, connect_robust
from aio_pika.abc import AbstractChannel, AbstractRobustConnection, ExchangeType

from src.core.rabbit.settings import RabbitSettings, rabbit_settings

T = TypeVar("T")


class AbstractRabbitPublisher(ABC):
	"""Abstract publisher."""

	settings: RabbitSettings = rabbit_settings

	def __init__(self, routing_key: str) -> None:
		self.routing_key = routing_key

	def _get_connection(self) -> Coroutine[Any, Any, AbstractRobustConnection]:
		return connect_robust(self.settings.rabbitmq_url)

	@abstractmethod
	async def publish(self, message: T) -> None:
		"""Publish message."""
		...


class WorkerRabbitSubPublisher(AbstractRabbitPublisher):
	async def publish(self, message: T, subscript_key: str | None = None) -> None:
		try:
			async with await self._get_connection() as connection:
				channel: AbstractChannel = await connection.channel()

				queue = await channel.declare_queue(self.routing_key, auto_delete=True)
				exchange = await channel.declare_exchange(self.routing_key, ExchangeType.FANOUT)
				await queue.bind(exchange, self.routing_key)

				# serialized_message = RootModel(message).model_dump_json()

				serialized_message = json.dumps(message)
				await exchange.publish(Message(body=serialized_message.encode()), subscript_key)
		except Exception as e:
			logging.error(f"Ошибка отправки сообщения: {e}")
			raise
