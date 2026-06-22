from fastapi import FastAPI

from .general import RoutersRegistry as GeneralRegistry


routers = [
    GeneralRegistry,
]


class RoutersRegistry:
    @staticmethod
    def register_routers(app: FastAPI) -> None:
        for router in routers:
            app.include_router(router.register_routers())
