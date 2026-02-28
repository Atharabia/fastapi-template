from fastapi import FastAPI

from . import health

routers = [health,]


class RoutersRegistry:
    @staticmethod
    def register_routers(app: FastAPI) -> None:
        for module in routers:
            app.include_router(module.router)
