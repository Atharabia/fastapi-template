from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.api import RoutersRegistry
from app.database import create_database_tables
from app.middleware import MiddlewareRegistry
from app.settings import Settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_database_tables()
    yield

app = FastAPI(
    title=Settings.APP_NAME,
    version=Settings.APP_VERSION,
    debug=Settings.APP_DEBUG,
    lifespan=lifespan,
    docs_url="/docs" if Settings.APP_DEBUG else None,
    redoc_url="/redoc" if Settings.APP_DEBUG else None,
    openapi_url="/openapi.json" if Settings.APP_DEBUG else None,
)

MiddlewareRegistry.add_middlewares(app)
RoutersRegistry.register_routers(app)
