from collections import Counter
import math
import re
from typing import Any
from fastapi import UploadFile

from src.core.redis import redis_tools


async def get_tf_idf(content: UploadFile) -> list[dict[str, Any]]:
	words_counter = Counter()
	result = []
	all_docs = redis_tools.increment_docs()
	text = await content.read()

	words = re.findall(r"\w+", text.decode().lower())
	words_counter.update(words)
	sum_all_words = sum(words_counter.values())

	for word, count in words_counter.items():
		tf = count / sum_all_words
		docs_count = redis_tools.increment_or_create(word)
		idf = math.log(all_docs / docs_count)

		result.append({"word": word, "tf": tf, "idf": idf})

	return sorted(result, key=lambda x: (-x["tf"], x["word"]))
