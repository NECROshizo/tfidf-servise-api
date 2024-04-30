from pydantic import BaseModel


class WordTFIDF(BaseModel):
	word: str
	tf: float
	idf: float


class ErrorSchema(BaseModel):
	error: str
