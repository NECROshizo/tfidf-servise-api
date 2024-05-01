from fastapi import APIRouter
from .v1 import router_api_v1
from .v2 import router_api_v2

main_router_api = APIRouter()

main_router_api.include_router(router_api_v1)

main_router_api.include_router(router_api_v2)
