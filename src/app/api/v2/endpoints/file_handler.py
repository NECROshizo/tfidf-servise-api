from fastapi import APIRouter, File, status, UploadFile

from src.app.api.validators import check_file_type
from src.app.api.shemas import ErrorSchema, WordTFIDF
from src.core.rabbit.publisher import WorkerRabbitPublisher


router = APIRouter()


@router.post(
	"/uploadfile/",
	summary="Загруска файла .txt для обработки",
	responses={
		status.HTTP_200_OK: {"model": list[WordTFIDF]},
		status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
	},
)
async def upload_file(file: UploadFile = File(...)) -> list[WordTFIDF]:
	"""Обработка файла"""
	await check_file_type(file.filename, ".txt")
	publisher = WorkerRabbitPublisher("in_worker")
	await publisher.publish(file)
	return [{"word": "ok", "tf": 33, "idf": 33}]
