from typing import Any, Optional

from pydantic import BaseModel


class Response(BaseModel):
    status: str
    message: Optional[str] = None
    data: Optional[Any] = None
