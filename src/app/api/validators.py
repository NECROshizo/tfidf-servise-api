from fastapi import HTTPException, status


async def check_file_type(file: str, file_type: str) -> None:
	if not file.endswith(file_type):
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail=f"Фаил должен быть разрешения {file_type}",
		)
