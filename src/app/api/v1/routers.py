from fastapi import APIRouter


from .endpoints import (
	file_router,
)

router_api_v1 = APIRouter(prefix="/v1", tags=["version 1"])

router_api_v1.include_router(
	file_router,
)
