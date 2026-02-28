from fastapi import APIRouter

from app.models.responses import Response

router = APIRouter(tags=["health"])


@router.get("/health")
def health_check() -> Response:
    return Response(status="SUCCESS", message="OK")
