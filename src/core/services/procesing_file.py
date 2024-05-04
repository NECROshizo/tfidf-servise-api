from collections import Counter
import math
import re
from typing import Any
from fastapi import UploadFile

from src.core.redis import redis_tools

CHUNK_SIZE = 1024


async def get_tf_idf(content: UploadFile, output_values: int = 50) -> list[dict[str, Any]]:
	words_counter = Counter()
	result = []

	async with redis_tools as redis:
		all_docs = await redis.increment_docs()
		while True:
			chunk = await content.read(CHUNK_SIZE)
			if not chunk:
				break
			words = re.findall(r"\w+", chunk.decode().lower())
			words_counter.update(words)

		sum_all_words = sum(words_counter.values())

		for word, count in words_counter.items():
			tf = count / sum_all_words
			docs_count = await redis.increment_or_create(word)
			idf = math.log(all_docs / docs_count)

			result.append({"word": word, "tf": tf, "idf": idf})

	return sorted(result, key=lambda x: (-x["tf"], x["word"]))[:output_values]
