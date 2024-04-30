from fastapi import APIRouter, File, UploadFile


router = APIRouter()


@router.post(
	"/uploadfile/",
	summary="Загруска файла .txt для обработки",
	# response_model=list[WordTFIDF]
)
async def upload_file(file: UploadFile = File(...)):
	"""Обработка файла"""

	return {"filename": file.filename}
