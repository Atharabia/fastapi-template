from fastapi import APIRouter

from app.controller import CONTROLLER_CLASS_NAME
from app.models.responses import Response

router = APIRouter(prefix="/ROUTER_PREFIX", tags=["ROUTER_TAG"])


@router.get("/")
async def ROUTER_FUNCTION_NAME() -> Response:
    return Response(status="SUCCESS")
