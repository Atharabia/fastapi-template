from sqlmodel.ext.asyncio.session import AsyncSession

from app.database import session


class CONTROLLER_CLASS_NAME:
    @session
    @staticmethod
    async def example(session: AsyncSession) -> None:
        ...
