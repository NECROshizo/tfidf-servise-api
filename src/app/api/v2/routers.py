from fastapi import APIRouter


from .endpoints import (
	file_router,
)

router_api_v2 = APIRouter(prefix="/v2", tags=["version 2"])

router_api_v2.include_router(
	file_router,
)
