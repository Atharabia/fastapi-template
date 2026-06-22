from fastapi import APIRouter

from app.models.responses import Response


router = APIRouter()


@router.get("/")
def get() -> Response:
    return Response(status="SUCCESS", message="OK")
