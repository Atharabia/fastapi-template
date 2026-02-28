from fastapi import FastAPI

from .cors import configure_debug_cors

middlewares = [configure_debug_cors]


class MiddlewareRegistry:
    @staticmethod
    def add_middlewares(app: FastAPI) -> None:
        for middleware in middlewares:
            middleware(app)
