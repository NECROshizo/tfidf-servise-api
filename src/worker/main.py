import asyncio

from src.worker.consumer import WorkerRabbitConsumer
# from app.worker.publisher import WorkerRabbitSubPublisher


async def main():
	worker = WorkerRabbitConsumer("in_worker")
	await worker.consume()
	# publisher = WorkerRabbitSubPublisher("revers_hell")
	# message = await worker.consume_one_message()
	# print(message)


if __name__ == "__main__":
	asyncio.run(main())
