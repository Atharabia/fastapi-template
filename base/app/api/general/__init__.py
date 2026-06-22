from fastapi import APIRouter

from . import health


class RoutersRegistry:
    router = APIRouter(prefix="/general")

    @classmethod
    def register_routers(cls) -> APIRouter:
        cls.router.include_router(health.router)
        return cls.router
