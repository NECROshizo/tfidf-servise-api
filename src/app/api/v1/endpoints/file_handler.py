from fastapi import APIRouter, File, status, UploadFile

from src.app.api.validators import check_file_type
from src.app.api.shemas import ErrorSchema, WordTFIDF
from src.core.services import get_tf_idf


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
	top_tf_idf = await get_tf_idf(file)
	return top_tf_idf
