from fastapi import APIRouter

from . import ROUTER_NAME


class RoutersRegistry:
    router = APIRouter(prefix="/ROUTER_PREFIX")

    @classmethod
    def register_routers(cls) -> APIRouter:
        cls.router.include_router(ROUTER_NAME.router)
        return cls.router
