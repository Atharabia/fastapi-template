from datetime import datetime
from datetime import timezone

from sqlmodel import Field
from sqlmodel import SQLModel


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class UserTable(SQLModel):
    __tablename__ = "user"
    id: int = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    password: str = Field()

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now,
                                 sa_column_kwargs={"onupdate": utc_now})
