from datetime import datetime

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database import UserTable
from app.database import session
from app.models.schemas import User


class UserController:
    @session
    @staticmethod
    async def get_user(session: AsyncSession,
                       email: str | None = None,
                       user_id: int | None = None) -> User | None:
        if email:
            statement = select(UserTable).where(UserTable.email == email)
        elif user_id:
            statement = select(UserTable).where(UserTable.id == user_id)
        else:
            return None

        result = await session.exec(statement)
        user = result.first()

        if user:
            return User(id=user.id,
                        email=user.email,
                        password=user.password)
        return None

    @session
    @staticmethod
    async def create_user(session: AsyncSession,
                          email: str,
                          password: str,
                          verification_code: str,
                          verification_expiry: datetime) -> UserTable:

        user = UserTable(email=email,
                         password=password,
                         verification_code=verification_code,
                         verification_expiary=verification_expiry)
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user
