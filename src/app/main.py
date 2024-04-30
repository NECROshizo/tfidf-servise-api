from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.app.api import main_router

app = FastAPI(redoc_url=None)

app.include_router(main_router)

templates = Jinja2Templates(directory="src/app/templates")


@app.get(
	"/",
	include_in_schema=False,
	response_class=HTMLResponse,
)
async def index(request: Request):
	"""Рендер формы загрузки файла"""
	return templates.TemplateResponse("upload_form.html", {"request": request, "upload_url": "/v1/uploadfile/"})
