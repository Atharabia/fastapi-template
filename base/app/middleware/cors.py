from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.settings import Settings


def configure_debug_cors(app: FastAPI) -> None:
    if Settings.APP_DEBUG:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
        )
